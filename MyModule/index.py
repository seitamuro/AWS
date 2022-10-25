# 作成したマクロのコード
def handle(event, context):
    if "Resources" not in event["fragment"]:
        return {
            "requestId": event["requestId"],
            "status": "success",
            "fragment": event["fragment"]
        }

    log_groups = {}
    for key, resource in event.get("fragment", {}).get("Resources", {}).items():
        if resource.get("Type") == "AWS::Lambda::Function":
            log_groups[f"{key}LogGroup"] = {
                "Type": "AWS::Logs::LogGroup",
                "Properties": {
                    "LogGroupName": {
                        "Fn::Sub": ["/aws/lambda/${FuncName}", {"FuncName": {"Ref": key }}]
                    },
                    "RetentionInDays": event["templateParameterValues"].get("LogRetentionDays", 365), 
                }
            }
    
    event["fragment"]["Resources"].update(log_groups)
    return {
        "requestId": event["requestId"],
        "status": "success",
        "fragment": event["fragment"]
    }
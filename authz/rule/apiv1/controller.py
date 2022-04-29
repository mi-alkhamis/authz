class ControllerAccessRules:
    __Controller_allowed_rules = {
        "get_user_list": ["admin", "service"],
        "get_user": ["admin", "service", "member:user_id"],
        "create_user": ["all"],
        "update_user": ["admin", "member:user_id"],
        "delete_user": ["admin"],
    }

    def get_controller_allowed_rules(f):
        return ControllerAccessRules.__Controller_allowed_rules[f]

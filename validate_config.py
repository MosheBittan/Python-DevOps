'''
Configuration Validator
Exercise: Configuration Validator

You are a DevOps engineer responsible for an automated deployment pipeline. A common source of failure is a malformed configuration file. To improve the reliability of your deployments, your task is to create a Python function that validates a configuration dictionary before the deployment process begins. This function will act as a "gatekeeper," preventing bad configurations from ever reaching production.



Problem Description

Your task is to implement the body of the validate_config function in the exercise.py file. This function will accept a single dictionary argument, config, and check it against a set of predefined rules.



Validation Rules

A configuration dictionary is considered valid only if it meets all of the following criteria:

Required Keys: It must contain the keys: service_name, env, and port.

Environment Value: The value for the env key must be one of the following strings: 'dev', 'staging', or 'prod'.

Service Name: The value for the service_name key must be a non-empty string.

Port Number: The value for the port key must be an integer between 1 and 65535 (inclusive).

If the configuration is valid, the function should return True. If it fails any of these checks, it should return False.

'''

def validate_config(config: dict) -> bool:
    requirment_keys = {key for key in config if (key in  ('env','port','service_name'))}
    env_values = {key:value for key,value in config.items()  if (key == 'env') and (value in ('dev' ,'staging','prod'))}
    if not env_values: 
        return False

    if len(requirment_keys)<3:
        return False
        
    for key,value in config.items():
        if key == 'port':
            if not (isinstance(value, int)):
                return False
            elif not (int(value) >= 1 and int(value) <= 65535):
                return False
        if key == 'service_name':
            if not value:
                return False
    
    return True
    

test1 = {
    'service_name': 'auth-service',
    'env': 'prod',
    'port': 8080
}
print (f"test1:{validate_config(test1)}")

test2 = {
    'service_name': 'auth-service',
    'env': 'production', # 'production' is not an allowed value
    'port': 8080
}

print (f"test2:{validate_config(test2)}")

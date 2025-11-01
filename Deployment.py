class Deployment:
    """
    Manages the state and version history of a software deployment.
    """
    def __init__(self, service_name: str, environment: str):
        self.service_name = service_name
        self.environment = environment
        self.status = 'pending'
        # This list is the "source of truth" for the deployment's version.
        # The underscore prefix `_history` is a convention indicating it's
        # an internal attribute not meant for direct external use.
        self._history = []
 
    def deploy(self, new_version: str):
        # A deployment simply adds a new "state" to our history.
        self._history.append(new_version)
        self.status = 'deployed'
 
    def rollback(self) -> bool:
        # A rollback is only possible if there are at least two versions in the history.
        if len(self._history) < 2:
            return False
        
        # list.pop() removes the last item (the current version),
        # effectively reverting to the one before it.
        self._history.pop()
        self.status = 'rolled_back'
        return True
 
    def check_status(self) -> dict:
        # The current version is always derived from the history list.
        current_version = self._history[-1] if self._history else None
        return {
            'service_name': self.service_name,
            'environment': self.environment,
            'version': current_version,
            'status': self.status,
        }

###### Test the Class : Deployment ####
test = Deployment("nginx","prod")
print(test.check_status())
test.deploy("1.0")
test.deploy("2.0")
print(test.check_status())
test.rollback()

class FireWall():
    rule_id = 0

    """Build you own firewalls with you rules"""
    def __init__(self,name):
        """Initiate the first build your FW
        Args:
            fw_name(str):the name of your fw
        """
        self.name=name
        self.rules = {}
        print(f"Initiate your firewall :{name}")

    def addRule(self, source_ip, destination_ip, action, rule_id=rule_id):
        """add new rule for your firewall , SOURCE IP ; DESTINATION IP ; ACTION (ALLOW,DENY)
        Args:
            source_ip(str):give a source ip in string
            destination_ip(str):give a destination ip in string
            action(str): action - ALLOW or DENY
        """
        # {"id":Z,"source_ip":"x.x.x.x" , "destination_ip":"y.y.y.y" ,"action":"ALLOW/DENY"}
        self.rules[rule_id] = {self.source_ip=source_ip,self.destination_ip=destination_ip,self.action=action}
        rule_id+=1
    
    def status(self):
        print(f"FW name:{self.name}")
        for rule in self.rules:
            print(f"ID is :{self.rule.id}, Source IP :{self.source_ip} , Destination IP:{self.destination_ip} , Action:{self.action}")


new_fw = FireWall("moshe")

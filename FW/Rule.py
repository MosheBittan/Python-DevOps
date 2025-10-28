class Rule():
    list_id: list = [] # contain list of IDS

    def checkID(cls,id:int):
        return id in cls.list_id
    
    def __init__(self,id,srcip,dstip,action):
        # --- THIS IS THE SOLUTION ---
        # 1. Check the ID *before* doing anything else.
        #    We can call the class method using 'Rule.checkID()'

        if Rule.checkID(id):
            raise ValueError(f"Error: Rule ID {id} already exists. Please use a new ID.")
        
        # -----------------------------

        # If the code reaches here, the ID is new and valid.
        print(f"ID {id} is new, creating rule...")
        
        # 3. Now we can safely create the object
        self.id = id
        self.srcip = srcip
        self.dstip = dstip
        self.action = action.upper()
        
        # 4. And add the new ID to the class list
        Rule.list_id.append(self.id)


    
 

moshe_new = Rule(1,"1.1.1.1","2.2.2.2","ALLOW")

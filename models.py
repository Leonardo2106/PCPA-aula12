from datetime import date

class Lead:
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created_at = date.today().isoformat()

        def model_lead(self):
            return {
                "name":self.name,
                "company":self.company,
                "email":self.email,
                "stage":self.stage,
                "created_at":self.created_at
            }
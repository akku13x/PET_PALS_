from dao.i_adoptable import IAdoptable

class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        return "Adoption event hosted!"

    def register_participant(self, participant: IAdoptable):
        self.participants.append(participant)
class Conference:
    def __init__(self, name, capacity):
        self.__name = name
        if capacity <= 0:
            raise ValueError('Вместимость посетителей должна быть больше 0')
        self.__capacity = capacity


    @property
    def name(self):
        return self.__name


    @property
    def capacity(self):
        return self.__capacity


    def has_available_seats(self, current_participants_count):
        return current_participants_count < self.__capacity 
 


class Participant:
    def __init__(self, name, email):
        if not name or not isinstance(name, str):
            raise ValueError("Укажите имя")    
        if not self._is_valid_email(email):
            raise ValueError("Неверный формат Email")
        
        self.__name = name
        self.__email = email

    def __eq__(self, other):
        if not isinstance(other, Participant):
            return False
        return self.email == other.email    

    def _is_valid_email(self, email):
        return '@' in email and '.' in email.split('@')[-1]    

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email
    


class RegistrationSystem:
    def __init__(self, conference):
        self.conference = conference
        self.participants = []

    def is_registration_available(self):
        return self.conference.has_available_seats(len(self.participants))

    def register(self, participant):
        if not self.is_registration_available():
            raise Exception('Нет свободных мест')
        if participant in self.participants:
            raise Exception('Пользователь уже зарегистрирован')
        
        self.participants.append(participant)




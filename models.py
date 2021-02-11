class Employee(object):

    def __init__(self, name, email, pay_day):
        validation(email)

        self.name = name
        self.email = email
        self.pay_day = pay_day

        self.save_email()

    def work(self):
        return "I come to the office."

    def check_salary(self, day):
        money = self.pay_day * day
        return money

    def save_email(self):
        emails_file = open('E-mails.txt', 'a')
        emails_file.write(f'{self.email}\n')
        emails_file.close()


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return "Должность: {} Имя: {}".format(self.__class__.__name__, self.name)


class Programmer(Employee):
    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return "Должность: {} Имя: {}".format(self.__class__.__name__, self.name)


class Candidate(object):
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException('I’m not hired yet, lol.')


class Vacancy(object):
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


def validation(email):
    file_e = open('E-mails.txt', 'r')
    for line in file_e.readlines():
        if line.strip('\n') == str(email):
            raise ValueError("This e-mail already exists")
    file_e.close()


class UnableToWorkException(Exception):
    pass

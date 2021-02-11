from models import *
from datetime import datetime
import traceback


def main():

    cand_1 = Candidate(full_name="Dila Ja", email="dila@gmail.com",
                       technologies="Py", main_skill="Programmer", main_skill_grade=5)
    cand_2 = Candidate(full_name="Sasha Smit", email="sanya@gmail.com",
                       technologies="C", main_skill="Programmer", main_skill_grade=3)
    cand_3 = Candidate(full_name="Ignat Mir", email="ign01@gmail.com",
                       technologies="C#", main_skill="Programmer", main_skill_grade=4)
    rcr = Recruiter(name="Tomas", email="tom@gmail.com", pay_day=45)
    prog_1 = Programmer(name="Alex", email="al@gmail.com", pay_day=40)
    prog_2 = Programmer(name="Yan", email="yan@gmail.com", pay_day=50)
    vac_1 = Vacancy(title="Programmer vacancy", main_skill="Programmer", main_skill_level=4)
    vac_2 = Vacancy(title="Recruiter vacancy", main_skill="Recruiter", main_skill_level=4)

    return rcr, prog_1, prog_2, cand_1, cand_2, cand_3, vac_1, vac_2


try:
    main()
except UnableToWorkException as exc:
    log = open('logs.py', 'a')
    a = traceback.format_exc().splitlines()
    log.write(f"{datetime.today()} UnableToWorkException, {exc}\n")
    log.close()
except ValueError as exc:
    log = open('logs.py', 'a')
    # a = traceback.format_exc().splitlines()
    log.write(f"{datetime.today()} ValueError, {exc}\n")
    log.close()

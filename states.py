from aiogram.fsm.state import State, StatesGroup

class Registor(StatesGroup):
    ism = State() # Temur
    familiya = State() # Valiyev 
    yosh = State()
    tel = State()
    kurs = State()
    viloyat = State()
    tuman = State()
    kocha = State()
    maktab = State()


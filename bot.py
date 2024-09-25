import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import Registor

TOKEN = "bot_token"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Ro'yxatdan o'tish botga hush kelibsiz"
    await message.answer(text)

@dp.message(Command("reg"))
async def register(message: Message, state:FSMContext):
    await message.answer("Ro'yxatdan o'tish uchun ma'limotlarni kiriting !  \nIsmingizni kiriting ")
    await state.set_state(Registor.ism)

@dp.message(F.text, Registor.ism)
async def register_ism(message: Message, state:FSMContext):
    ism = message.text   # Temur
    # {"name": "Temur"}
    await state.update_data(name = ism)
    await state.set_state(Registor.familiya)
    await message.answer("Familiyani kiriting")

@dp.message(F.text, Registor.familiya)
async def register_familiya(message: Message, state:FSMContext):
    familiya = message.text  # Valiyev
    # {"name": "Temur", "surname" : "Valiyev"}
    await state.update_data(surname = familiya)
    await state.set_state(Registor.yosh)
    await message.answer("Yoshingizni kiriting")



@dp.message(F.text, Registor.yosh)
async def register_yosh(message: Message, state:FSMContext):
    yosh = message.text  # "12"
    # {"name": "Temur", "surname" : "Valiyev", "age": "12"}
    await state.update_data(age = yosh)
    await state.set_state(Registor.tel)
    await message.answer("Telefon raqamni kiriting")

@dp.message(F.text, Registor.tel)
async def register_tel(message: Message, state:FSMContext):
    tel = message.text   # +998974020330
    # {"name": "Temur", "surname" : "Valiyev", "age": "12", "tel": "+998974020330"
    

    await state.update_data(tel = tel)
    await state.set_state(Registor.kurs)
    await message.answer("Kursni nomini kiriting")

@dp.message(F.text, Registor.kurs)
async def register_kurs(message: Message, state:FSMContext):
    kurs = message.text
    await state.update_data(kurs = kurs)
    await state.set_state(Registor.viloyat)
    await message.answer("Viloyat nomini kiriting")

@dp.message(F.text, Registor.viloyat)
async def register_viloyat(message: Message, state:FSMContext):
    viloyat = message.text
    await state.update_data(viloyat = viloyat)
    await state.set_state(Registor.tuman)
    await message.answer("Tuman nomini kiriting")

@dp.message(F.text, Registor.tuman)
async def register_tuman(message: Message, state:FSMContext):
    tuman = message.text
    await state.update_data(tuman = tuman)
    await state.set_state(Registor.kocha)
    await message.answer("Kocha nomini kiriting")

@dp.message(F.text, Registor.kocha)
async def register_kocha(message: Message, state:FSMContext):
    kocha = message.text
    await state.update_data(kocha = kocha)
    await state.set_state(Registor.maktab)
    await message.answer("Maktabingizni kiriting")

@dp.message(F.text, Registor.maktab)
async def register_maktab(message: Message, state:FSMContext):
    data = await state.get_data()


    # baza = {"name": "Temur", "surname" : "Valiyev", "age": "12", "tel": "+998974020330"}

    data = await state.get_data() # Ma'lumotlarni (ba'zadan) olish

    # ba'zadan ma'lumotlarni olish
    ism = data.get("name")
    familiya = data.get("surname")
    yosh = data.get("age")
    tel = data.get("tel")
    kurs = data.get("kurs")  # Python
    viloyat = data.get("viloyat")
    tuman = data.get("tuman")
    kocha = data.get("kocha")
    maktab = message.text


    text = f"Ism : {ism} \nFamiliya : {familiya} \nYosh : {yosh} \nTel : {tel} \nKurs : {kurs} \nViloyat: {viloyat} viloyati \nTuman: {tuman} tumani \nKo'cha: {kocha} ko'chasi \nMaktab: {maktab}"
    await message.answer("Siz ro'yxatdan o'tdingiz")
    # # --------------1ta adminga malumotlarni yuborish--------------
    # await bot.send_message(chat_id= 7241341727, text=text  )

    # # --------------ADMINLARGA KODNI YUBORISH---------------
    admin1 = "id1"
    admin2 = "id2"
    await bot.send_message(chat_id= admin1, text=text)
    await bot.send_message(chat_id= admin2, text=text)
    await state.clear()

    
async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

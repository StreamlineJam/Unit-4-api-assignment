from fastapi import FastAPI
import uvicorn

total_run_count = 0

app = FastAPI()

APP_KEY = "UDHFTGHVCJUDI"

fruits = [
    {"fruit": "apple", "color": "red"},
    {"fruit": "orange", "color": "orange"},
    {"fruit": "Grapes", "color": "purple"},
]

Grade = [
    {"man": "Leon", "Grade": 75},
    {"man": "Richard", "Grade": 95},
    {"man": "Harry", "Grade": 95}
]

Genders = [
    {"gender": "attack helicopter", "number": 1},
    {"gender": "Speedboat", "number": 2},
    {"gender": "Ipad", "number": 3}
]

Computers = [
    {"computer": "Macbook", "usefulness": 1},
    {"computer": "windows", "usefulness": 4},
    {"computer": "linux", "usefulness": 0}
]

Writing_Tools = [
    {"writing tool": "pencil", "price": 1},
    {"writing tool": "pen", "price": 5},
    {"writing tool": "Brush", "price": 3}
]

Phones =[
    {"phone": "Huawei", "patriotness": "I love China"},
    {"phone": "iPhone", "patriotness": "execution date: tmrw"},
    {"phone": "Xiaomi", "patriotness": "5G"}
]

Drinks =[
    {"drink": "coke", "deliciousness": "very"},
    {"drink": "sprite", "deliciousness": "very"},
    {"drink": "water", "taste": "meh"}
]

Book =[
    {"book": "paper", "fun": "meh"},
    {"book": "ebook", "fun": "its alr"},
    {"book": "scrolls", "fun":"ok"}
]

Food =[
    {"food": "steak", "taste": "ok"},
    {"food": "chicken", "taste": "ok"},
    {"food": "soup", "taste" : "horrid"}
]

Tissue =[
    {"tissue": "rough", "feeling": "not ok"},
    {"tissue": "smooth", "feeling": "sick"},
    {"tissue": "garbage", "feeling": "horrible"}
]

Woah_easter_egg =[
    {"wa": "wow", "woah": "huh"},
    {"wa": "face", "OMO": "another face"},
    {"wa": "woaaah", "what 20 items?!?": "how about 20 items with same pairs"}
]

Woah_easter_egg_2 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_3 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_4 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_5 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_6 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_7 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_8 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_9 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]

Woah_easter_egg_10 =[
    {"wa": "wow", "wo": "huh"},
    {"wa": "face", "wo": "another face"},
    {"wa": "woaaah", "wo": "how about 20 items with same pairs"}
]






@app.get("/fruits/get_info")
async def get_fruits(fruit: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for fruits_info in fruits:
        if fruit.lower() == fruits_info['fruit'].lower():
            return fruits_info
    return {"msg": "fruit not found"}


@app.get("/grade/get_info")
async def get_grade(grades: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for grades_info in Grade:
        if grades.lower() == grades_info['man'].lower():
            return grades_info
    return {"msg": "grade not found"}

@app.get("/gender/get_info")
async def get_gender(genders: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for gender_info in Genders:
        if genders.lower() == gender_info['gender'].lower():
            return gender_info
    return {"msg": "gender not found"}

@app.get("/computer/get_info")
async def get_computer(computers: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for computer_info in Computers:
        if computers.lower() == computer_info['computer'].lower():
            return computer_info
    return {"msg": "computer not found"}

@app.get("/writing tools/get_info")
async def get_tools(tools: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for tools_info in Writing_Tools:
        if tools.lower() == tools_info['writing tool'].lower():
            return tools_info
    return {"msg": "tool not found"}


@app.get("/phone/get_info")
async def get_phone(phone: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for phone_info in Phones:
        if phone.lower() == phone_info['phone'].lower():
            return phone_info
    return {"msg": "Phone not found"}

@app.get("/drinks/get_info")
async def get_drinks(drinks: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for drinks_info in Drinks:
        if drinks.lower() == drinks_info['drink'].lower():
            return drinks_info
    return {"msg": "drink not found"}

@app.get("/books/get_info")
async def get_books(books: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for books_info in Book:
        if books.lower() == books_info['book'].lower():
            return books_info
    return {"msg": "drink not found"}

@app.get("/food/get_info")
async def get_food(foods: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for food_info in Food:
        if foods.lower() == food_info['food'].lower():
            return food_info
    return {"msg": "food not found"}

@app.get("/tissue/get_info")
async def get_tissue(tissues: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for tissue_info in Tissue:
        if tissues.lower() == tissue_info['tissue'].lower():
            return tissue_info
    return {"msg": "tissue not found"}

@app.get("/easter_egg/get_info")
async def get_easter_egg(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_2/get_info")
async def get_easter_egg_2(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_2:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_3/get_info")
async def get_easter_egg_3(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_3:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_4/get_info")
async def get_easter_egg_4(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_4:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_5/get_info")
async def get_easter_egg_5(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_5:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_6/get_info")
async def get_easter_egg_6(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_6:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_7/get_info")
async def get_easter_egg_7(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_7:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_8/get_info")
async def get_easter_egg_8(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_8:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_9/get_info")
async def get_easter_egg_9(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_9:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}

@app.get("/easter_egg_10/get_info")
async def get_easter_egg_10(eggs: str, appid: str):
    if appid != APP_KEY:
        return {"msg": "Key is incorrect"}
    for egg_info in Woah_easter_egg_10:
        if eggs.lower() == egg_info['wa'].lower():
            return egg_info
    return {"msg": "egg not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

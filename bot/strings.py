
from states import Education, NeedEmployee, NeedEmployeeForSchool, NeedJob, NeedStudent, NeedTeacher


MENUS=["Xodim kerak", 
        "Ustoz kerak", "Shogird kerak", 
        "O’quv kurslari", 
        "Ish joyi kerak"]

START="""
<b>Assalom alaykum {name}!</b>
Ta'lim link kanalining rasmiy botiga xush kelibsiz!

<i>Eslatma:</i> Kanalga o'quv markazlarining o'quv kurslari haqidagi e'lonlardan tashqari boshqa barcha e'lonlarni bepul joylashtirishingiz mumkin.  
O'quv markazlarining o'quv kurslari haqidagi e'lonlar masalasida esa adminga bog'lanishingiz lozim bo'ladi. 
/help yordam buyrug'i orqali bot nimalarga qodir ekanligini bilib oling!
"""


HELP="""
Ta'lim link kanalining maqsadi va ish faoliyati haqida qisqacha ma'lumot. 

Ushbu kanalda siz o'zingiz uchun ustoz, hamda tajribali xodim topishingiz mumkin.
Shuningdek, maktab va o'quv markazlaridagi bo'sh ish o'rinlari haqida e'lon joylashtirishingiz ham mumkin.
Kanalning afzallik jihatlaridan yana biri shundaki, sizda kadrlarni va ish o'rinlarini tanlash imkoni paydo bo'ladi.
Endi ish yoki o'quv markazi qidirib ko'chama-ko'cha yurib sarson bo'lmaysiz. 📱Telefonda bizning kanal orqali, 🏠 uydan chiqmagan holda ham bu masalalarni hal etishingiz mumkin bo'ladi. 
Niyatimiz yurtimiz fuqarolariga yanada yengillik yaratish, ishsizlik hamda sifatli ta'lim olish masalalari hal bo'lishida oz bo'lsada o'z hissamizni qo'shish.

Ta'lim e'lonlarini bizning kanaldan izlang. 
Ta'limga tikilgan sarmoya hech qachon besamar ketmaydi
"""


TEXT="""<b>{type} topish uchun ariza berish\n</b>
Hozir sizga bir necha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to'g'ri bo'lsa, Tasdiqlash tugmasini bosing va arizangiz Adminga yuboriladi."""


EMPLOYEE={
    "center":("<b>🏢 O'quv markaz:</b>","\nO'quv markaz nomini kiriting. Masalan, <i>Target</i>"),
    "subject":("<b>📗 Fan(lar):</b>","\nFan(lar) nomini kiriting. Masalan, <i>Ingliz tili</i>"),
    "telegram":("<b>📱 Telegram:</b>","\nTelegram:"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog'lanish uchun raqamingizni kiriting. Masalan, <i>+99890 123-45-67</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "responsible":("<b>✍️ Mas'ul:</b>","\nMas'ul shaxsning ismini kiriting"),
    "working_hours":("<b>🕰 Ish vaqti:</b>","\nIsh vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "app_time":("<b>🕰 Murojaat vaqti:</b>","\nMurojaat qilish vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "salary":("<b>💰 Maosh</b>","\nQancha miqdorda maosh to'lanishini kiriting. Masalan, <i>2.5 mln</i>"),
    "addition":("<b>📜 Qo`shimcha:</b>","\nQo'shimcha ma'lumot bo'lsa kiriting:"),
}

TEACHER={
    "student":("<b>🎓 Shogird:</b>","\nIsm, familiyangizni kiriting:"),
    "age":("<b>🌐 Yosh:</b>","\nYoshingizni kiriting. Masalan, <i>21</i>"),
    "subject":("<b>📗 Fan:</b>","\nTalab qilinadigan fanlarni kiriting?. Fan nomlarini vergul bilan ajrating. Masalan, <i>Ingliz tili, matematika</i>"),
    "telegram":("<b>📱 Telegram:</b>","\nTelegram:"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog'lanish uchun raqamingizni kiriting. Masalan, <i>+998901234567</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "price":("<b>💰 Narxi:</b>","\nTo'lov qilasizmi yoki Tekinmi?. Summani kiriting:"),
    "job":("<b>👨🏻‍💻 Kasbi:</b>","\nIshlaysizmi yoki o`qiysizmi? Masalan, <i>Talaba</i>"),
    "app_time":("<b>🕰 Murojaat qilish vaqti:</b>","\nMurojaat qilish vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "target":("<b>🔎 Maqsad:</b>","\nMaqsadingizni qisqacha yozib bering."),
}

STUDENT={
    "teacher":("<b>🎓 Ustoz:</b>","\nIsm, familiyangizni kiriting:"),
    "age":("<b>🌐 Yosh:</b>","\nYoshingizni kiriting. Masalan, <i>21</i>"),
    "subject":("<b>📗 Fan:</b>","\nTalab qilinadigan fanlarni kiriting?. Fan nomlarini vergul bilan ajrating. Masalan, <i>Ingliz tili, matematika</i>"),
    "telegram":("<b>📱 Telegram:</b>","\nTelegram:"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog`lanish uchun raqamingizni kiriting. Masalan, <i>+998901234567</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "price":("<b>💰 Narxi:</b>","\nTo'lov qilasizmi yoki Tekinmi?. Summani kiriting:"),
    "job":("<b>👨🏻‍💻 Kasbi:</b>","\nIshlaysizmi yoki o`qiysizmi? Masalan, <i>Talaba</i>"),
    "app_time":("<b>🕰 Murojaat qilish vaqti:</b>","\nMurojaat qilish vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "target":("<b>🔎 Maqsad:</b>","\nMaqsadingizni qisqacha yozib bering."),
}

EDUCATION={
    "center":("<b>🏢 O'quv markaz:</b>","\nO'quv markaz nomini kiriting. Masalan, <i>Target</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "subject":("<b>📗 Fan(lar):</b>","\nFan(lar) nomini kiriting. Masalan, <i>Ingliz tili</i>"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog'lanish uchun raqamingizni kiriting. Masalan, <i>+99890 123-45-67</i>"),
    "telegram":("<b>📱 Telegram:</b>","\nTelegram:"),
    "price":("<b>💰 Narxi:</b>","\nSummani kiriting:"),
    "payment":("<b>💰 To'lov turi:</b>","\nTo'lov qanday amalga oshiriladi (naqd, pul ko'chirish)"),
    "addition":("<b>📜 Qo`shimcha:</b>","\nQo'shimcha ma'lumot bo'lsa kiriting:"),
}

JOB = {
    "employee":("<b>👨‍💼 Xodim:</b>","\nIsm familiyangizni kiriting:"),
    "age":("<b>🕑 Yosh:</b>","\nYoshingizni kiriting. Masalan, 19 yosh:"),
    "subject":("<b>📚 Fan(lar):</b>","\nFanlar nomini kiriting"),
    "telegram":("<b>🇺🇿 Telegram:</b>","\nTelegram"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog`lanish uchun raqamingizni kiriting. Masalan, <i>+998901234567</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "job":("<b>👨🏻‍💻 Kasbi:</b>","\nIshlaysizmi yoki o`qiysizmi? Masalan, <i>Talaba</i>"),
    "app_time":("<b>🕰 Murojaat qilish vaqti:</b>","\nMurojaat qilish vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "target":("<b>🔎 Maqsad:</b>","\nMaqsadingizni qisqacha yozib bering."),
    "addition":("<b>📜 Qo'shimcha malumotlar:</b>","\nQo'shimcha ma'lumot bo'lsa kiriting:"),
}

SCHOOLEMPLOYEE={
    "school":("<b>🏢 Maktab(Nomer):</b>","\nNechinchi maktab?"),
    "subject":("<b>📗 Fan(lar) dars soati:</b>","\nFanlar nomini va dars soatini kiriting:"),
    "telegram":("<b>🇺🇿 Telegram:</b>","Telegram"),
    "contact":("<b>☎️ Aloqa:</b>","\nBog`lanish uchun raqamingizni kiriting. Masalan, <i>+998901234567</i>"),
    "address":("<b>Ⓜ️ Manzil:</b>","\nManzilni kiriting. Masalan, <i>Toshkent shahri, Olmazor tumani</i>"),
    "app_time":("<b>🕰 Murojaat vaqti:</b>","\nMurojaat qilish vaqtini kiriting. Masalan, <i>08:30 dan 17:00 gacha</i>"),
    "addition":("<b>📜 Qo`shimcha:</b>","\nQo'shimcha ma'lumot bo'lsa kiriting:"),

}

STATES={
    "Xodim kerak":NeedEmployee,
    "Ustoz kerak":NeedTeacher,
    "Shogird kerak":NeedStudent,
    "O’quv kurslari":Education,
    "Ish joyi kerak":NeedJob,
    "Xоdim kerak":NeedEmployeeForSchool,
}

FORMS={
    "Xodim kerak":EMPLOYEE,
    "Ustoz kerak":TEACHER,
    "Shogird kerak":STUDENT,
    "O’quv kurslari":EDUCATION,
    "Ish joyi kerak":JOB,
    "Xоdim kerak":SCHOOLEMPLOYEE,
}

TITLE={
    "Xodim kerak":"<b>🏬 TAJRIBALI XODIM KERAK</b>",
    "Ustoz kerak":"<b>👨‍💻 USTOZ KERAK</b>",
    "Shogird kerak":"<b>👨‍💻 Shogird kerak:</b>",
    "O’quv kurslari":"<b>🏬 O'quv kurslari</b>",
    "Ish joyi kerak":"<b>🏬 ISH JOYI KERAK</b>",
    "Xоdim kerak":"<b>🏬 Maktabga xodim kerak</b>"
}

TAG={
    "Xodim kerak":"#ishJoyi",
    "Ustoz kerak":"#shogird",
    "Shogird kerak":"#ustoz",
    "O’quv kurslari":"#õquvKursi",
    "Ish joyi kerak":"#xodim",
    "Xоdim kerak":"#ishJoyiMaktab"
}

STATE_NAMES={
    "NeedEmployee":"Xodim kerak",
    "NeedTeacher":"Ustoz kerak",
    "NeedStudent":"Shogird kerak",
    "Education":"O’quv kurslari",
    "NeedJob":"Ish joyi kerak",
    "NeedEmployeeForSchool":"Xоdim kerak",
}

SENDEDTOADMIN="""
<b>📬 So'rovingiz tekshirish uchun adminga jo'natildi!</b>

E'lon 24-48 soat ichida kanalga chiqariladi.
"""
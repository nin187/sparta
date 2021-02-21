import hgtk

misugang_nakoja_list = [
    "이현주",
    "이후석",
    "감사소희",
    "김태진",
    "최은미",
    "정현석",
    "마수영",
    "이기호",
    "정진태",
    "은재",
]
for nakoja in misugang_nakoja_list:
    name_josa = hgtk.josa.attach(nakoja, hgtk.josa.EUN_NEUN)
    print(f"나 {name_josa} 인생의 낙오자 입니다.")

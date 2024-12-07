from suno import Suno, ModelVersions
client = Suno(
    cookie='_ga=GA1.1.1756958524.1729511773; ajs_anonymous_id=6cdc446a-63b9-43bb-b3a0-72229b407416; __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8ybmtLanlhZmo5dUtqU2lUb09KWkt6ZmNNWUsiLCJyb3RhdGluZ190b2tlbiI6ImJueWwwZTlpOWRvMmR3dDF6dzQ5amM4Mmx1cTJicGptc3NwMnR5MmYifQ.rQM9yzZh6xlp0WUwld3R4rdr32BxZN4gjcLCSPQaw1buQNmJH1bZz8NCvCVcT8j0eub7J50DySn_U6ea3rT5sctZZtUsycSAomFbEwZASb1OdgzGuk-gAtPNUyjh01YT2so_9cFj-Vwn6PkK_7t0f6EsvVlE_u59eJPTuLIliPl814-5NKa8QoyOUHt44Wbhr31Reo5CJrQKb0WOo_CpxI-4vtvT2QApsnIX0pjKklXybWxsF_pikM19aqOix0hGDoHf2qCVVKq5iYwJXAv33FoyFyR_926WdTuR0geRepr6os_l31cMT66lC5jEOaEJcst5vpUwl3GwF6BIZSeyLA; __client_uat=1730872630; __client_uat_U9tcbTPE=1730872630; __stripe_mid=33561d60-9def-486e-b7cb-938a3fdaaba6c794d4; __cf_bm=eeSd7C8_ygjbwWguPIAAl8mpLEXukePMh7sYYyY84n4-1733380076-1.0.1.1-IMPYKJDi5VYW4Ajcf3AFxo0cgmWfzq1N60hl6LJhwx7D_RL01ePCXHIUXYlktBPO88BoGmejmKcvxETt2jzq2g; _cfuvid=FvDp0o1O5JIJeoSyDraPzAdFcZrfb7dy58bdTa.AiL4-1733380076679-0.0.1.1-604800000; _fbp=fb.1.1733380079765.86166798744832277; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22cb3f17e4-8fc9-4d24-b6ca-1c932d13bca5%22%2C%22%24device_id%22%3A%20%22192aeef4f9c66e-004e958ff3d5f9-4c657b58-144000-192aeef4f9c66e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24user_id%22%3A%20%22cb3f17e4-8fc9-4d24-b6ca-1c932d13bca5%22%7D; _ga_7B0KEDD7XP=GS1.1.1733380079.11.1.1733380761.0.0.0'
model_version=ModelVersions.CHIRP_V3_5)

# Generate a song
songs = client.generate(prompt="A serene landscape", is_custom=False, wait_audio=True)

# Download generated songs
for song in songs:
    file_path = client.download(song=song)
    print(f"Song downloaded to: {file_path}")
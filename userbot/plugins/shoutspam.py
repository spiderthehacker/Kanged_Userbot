"""Emoji
Available Commands:
.spem"""



from telethon import events



import asyncio











@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))



async def _(event):



    if event.fwd_from:



        return



    animation_interval = 9

    



    animation_ttl = range(0, 103)



    input_str = event.pattern_match.group(1)



    if input_str == "spem":



        await event.edit(input_str)



        animation_chars = [



            "DSGZ9vpTDLaIwwn8w3xNNxOxOxMTXoRc24cvtjHYZgIP7PGH2nYtZHAenRY1OFzdEz9nEMrBunYinRm9GuluDYwPflXF2mXC89yeNRmoVxLPTyuj1m4UrAvhBtTUFaWfb0lAWb8Hmr8NsY4QJQHW5M8PGWJyYEP9H7hnMpOMeuTdFZhvRiloEDMT4zCEIhPjnGZ4wB5A6QHsR6wbJEOYWUGw3FnUCT9ocKh5Nmpjhhy7EexFvza0gzPgmyRPmwEZPZbLLkaP2N1G8voCKVQ80VSAwwYcMkWTpOdDyucW2lLMCv1h03JGLjjlOfYHY3YOM7cItz7M7Q2KnUqoDvX8FzuHsmq6PeR0ZAx3ov2EZSTRhPbzv3Stg1T2ZttDB1SsdyQamlMa7PB2NxjlSBPc7j6xubsXgZHL8ndtv9BS2etJRf7fVkLhaSpLqF6W00tdQ7hTOZkmg3SwTOYj6232ufiFbpMuO9verqHmdDKnNwGFAn8tp3C7o7Wrn55z4TImcwgT2PZLqnUJ6uiRVpzOsxEa36tmvDgL7NGA4t6hfc2zEW4yxJehCkiC461AuFm9nzILNPTLS4FsUqDpA5ctCS7iYV5dk68g0h4gTAUCsqe7CqpaCWGdjjiy408fIVJcccsDiurLpTrCstzks475gKa5tSYyqBJFtmqQsgefXxXfibKMCApnS1yk2IAAiJRRXcmNu9953C9Cuh2Y6GbAuH3G9Hh82ve1ySiV9r7yosijIHgkp4jEiZbYspq990UaWyU7ZvKglEbnD3miOo52wSmz5tXiQtR2jwORNS11bssahsN1JL0qog0PwiB2UsihKwfVxPMp6zoPm9GHj2HwO0thwTnceBKJfhOmJ2Lzwxswk4k5ZA4ANaSv5VlvOlNa9EXeMWa0L4LO3JNnU8Jiqz4c7hQXmFgdSvx8kOg88ST8qyIwdXtv49ta04M98BRjaaDvGSWIvlFrUEAW8zl",

            "NHZ9KlWdkPrCbVcGni34aQYpPZWOJRzLpTTycmNUXFqt2KGcqN5Z4Eq4TR8rlc5xv7RLNortmxej256wAByhu4dQ1USyyy5ua9cLilqgYUCNzU5y1KwEw1RuvK746Phj4sGmzVgrndWp7jCmSJEt2M8YVq43wSSCIEszLku7OxUMiKlvktUkGtbZEsm0TK9capkg0WMzYnksW1lBoEspK71XxA45tg5ODLvs8Ro95LOZ23ytptsQ9g6TnHTy1Zoy3OHGvolkl9OABRfKjpqOJ0OTMl6P1vsuB5RHpNCsmTkPs0ZmEJqJErQ8pDljE8KlxBFjv6IjYOCevArmpfZL7wK81LCralpbcDr1wY5xUEDiWueelpqD6p6byRBcMBXIzPBn2ot6pbVm01IBM7DRFXp3IqpEFqiYSLBbcdU7qtIh8CO0UopZD4NLapvyhFrpdnESVAU306Yq3q2v6SbJyflo1kYFmcxDRzmR2i471oTjilXJj9rz2Cez9CQVhhMwnZJcH50gydSMyk10qJJ7GdJnAsNmsWV9KMdzrxxJHvfWilDQBLrv3fEb2j3CS4uIuQHlhtUhXVe4xvqna2U6odlesNgS0FAex2XqLsr0nuu0DwbiJwtoXW2QYD1lmQJeCUBRz8OiRFL5hKKf7Ur3PfvFSTuCstOoWkMDP7sJVEeLGgCLo0BT5ojzHX6td70vIdXzGh3ZHGY9b3PaYctNmAjYc8TcORTvrzDClfiqjHVJoQESy5tkw2fpSI28ebWa6iVw7TlBM7dN0fanE3w1CDp807FYhq2qAlbrFlLYJwqSAX6Nil2V7m4d8J8o7TXhyMfEeR7VSK6UPpIgQjUMUYvGiMutdsFHFsxlgGOhDk2URUZggHxLlg1o2235br2iLDnVFysSY9VHJ5ejeZSbljmjcroXmI0L3aDxJk2eM4AMHYzvG4Cyf4Qg8V06MiibsoM2nNoEepaN6Slmy8P",    

            "qSi8w8mm4WrA8mwZxtAMgvor29Oe4xXrA062zjjThRFbDJekiGsZX6WRIks41hL3plVpMZtcFwY7i9bvgLLzfaWbSWNiGgv61uF3lpd41InIiZRM8zYI75aLPtSvwqXN4SB2qNw2vA5VMqAp8LqiHEXSZzwcaLA9ksVSDrOzTa8kGGAcKBYm5AAIg4z5MyL3MJjdK4j4ksBqiBOlQ7VL0z9tAT2AM8EO2NscbVCgnhyZf9KqxSln1hkg5Garbo1lXY0IonVsGAxg45awmwfYriwwIwqeX2mWBwhjsE5EbK7DI2PNSJJX3vKAZgXMjal4A7LitgodBgkka4gNQNh6qTwLdi45fNhcMGoMbe5wxt9jnnaBP2uHfWS0FStFX4VJ5BGN6rqhCm4wrMZsWMQEupg6Mjvkk4BTfI4INcRZKbTBiBPtd6zr2uu0cQrYbImIp0RftctdZGLFgfEctMwnyVHx1VKreUpmUCufA2TKnpD2h1WPV6OximZE2l13EtpOn1n8d8RUBa1RxF3GAE8LdawyYwP51nCo62h8cjfsc3joxSmBoX7UZoCHpkjhElCWPU7TdDqJg1k0iyYhid3R0tUgs0blzoGAjkwY8k2bx9LsKUV0BQwL1TKy0C9wKANGy40W1BsczKzNbGVRTndwEWSPltYIR8i2zf1fW20Wo9abpMGQ9mmqNmXUKLwH2kojcauwtfy9zR61pYaBZyJqAPsVbEEd9bjyVl3GdRnIhWDrt4giMuY9ZXCKJrOa9cZfMvW77xLWH3NBb1lABIQkLrTrYEVrN7n2g6uvo4LOZ8XXG7ji4fCUk3aeJKxUzdTHhredjNHd8kk6UnEXaNvfCD4B22Bxj0N0NkiEwhU286WCM1mMfEer92Mo4nUp9t4P6QTFW04Hesp1RAcWZuCpXPZXI9FstgEskP9b0DWIvVgAi1i49DnlokmkHUPzZ1i0JlEvXmvcpX7GAs29lb1",

            "aOqASnai4NkZRqCQxz4iLTNX2B7WcTzivjNERBVFlzvqP40Lb8ab2rOte254g8gI3KOotqbRgvF5mN2b4Qviy6fSI4H18bXdciIiaMlex6aNQyMYDYgCoDPsbW9j747NpT56JIVz61R5lLEUXG5znbeIYPbXxaLsUIfvov8vouwGeRahhIlPPitHF4FlRHVbzZpUgMSmLBabNNo0FGniKJdUX0mgnRhkkhdnY9ECwXRvlCyUshj5PZuiWfn6pRr17WFYus2rX4uz9PIOXtWtH5T9PsbnjBfTy0qYJnI561JDxAE576encr1XAm5qylbCi0c4AKtax9HFlbaiH8ca2q1SBAAhMtpxsu0LMaCaM7RUA6hLv7Q6dC8RBUc2YVM1VmuS2dlaSBK8vnZumTcCO493xjUTWxANlHNBwEJ2pYmcn01ydDCNO0tyWXOVr3y4I1uyNWGHuOQqhwqEEBeG7J9yqWooz6FP1VgsWR7IamwZ8vsG4FABf0wQhwnDgL6DJF7racen9NAMyKzJtsausQ8uoYaGQ9Fo9uYH2QOsykHcEnWKThgEO0wjCakvqDfIQVSksCEwz9cR8xCpFxr9zndh4BQ30ZoDFad7CvVSHBTttDg4uIh1z0XFLDAM8C0YNV4sNqQIQRlpW5OTeqmFIyLZrygzQyQPidqi5lsRVUZeC1kH6P3B9AAF14MeQaO3mLz2DHlI7w6IWTnnElJoQoT9qhgQ43qBh1qhNUqim70TEL7hDPjivNidGLMw1MyvHkx6IP5xSwfYLJBZLUtsvOCE5Aph7afP7JYKU16ukjG3SS0NvLYYEHPGdMCDlLU3fri0ORcJkJTnSCZ0jITRd9KvNFlLzhwFreuXlqvapXbLSw2Re9tTedAYqauYukO8n6Y9RnU0nhLe9eLy3XjZRJxPGSRprMj03CXOUirpw3G0tCIWKQl3qyQJVkM8laEQFly5kPIf111TNdERbhS",

            "J36JQBnn8vGBci1HuEPuZFhCM6fw8W29FjiesElBFAB5dtIxDZKqEiVaIk3c88tKsFz1T3qHM4Kg2mnnZ0ugN1Zc7BGkB8VC2aCHQXhbtTVEzyk5DmKKDfzWGgnAZXB8fCKuByH8DBY2ewIhGAUv0ABK2Orgv3g71h6RfiYVM3GFr3gTf5bx3QA0ogaaoAF7OGyN0GlkuAgMMzCLUUahpRJ6pDtm9ghQGdFJTJKdddPcsSf3tkKCVgLym6Fs2LfHIy6Cw4VhDenlOWYtKsRZXyHnOvFcpwarr9QvXI4yX4colObjfn1uxC6opzLYsuz4bNn7b4V6UVG2Qm9QVHKoY5RpyxNCvByI7bEpXY3fxzSEL4EZkp863cBYJBiBUzy1GNF9VT4XK2jEKHrIzUhY4CRDqnq0J3LBmQab4gQboaAdKn6qFI5waUtnO742xfkWhKTHZGhFEAboJZJR2qD49EtOf2RafCE2nxnNNAojBZFmrfkI6eWOCcXI4WDmzmOxZGwAaDNa16FqnyIvXVZ4xLGfrPfblRHJHJ6G75Na2chd9Q8dYun3uDqfCheMLK0nPxnNGzkvR4usxrzKHBeXIIEEwyVWaldkCib6jw4AmJ8Ve4Ehukcg5KgpVhFWtXLLCElZbjxC5KdzJN8EcgziKmD1wPqYWzFn1tpNXDByQnC4QLnoArVmozcBHseDkXPl8PNrjDdF4aHfY7LT4mRVU2DEsjtSbYQYgsw7ackkMPFx4FaZ2IkNR6ebi8PRHn47xP2F2pdj25N0u36Nq0rcrjP4qAAmsdd9l44IL5xX6mJEJckSWaxH7EnmH3HHtBQKRoG0nBuihp6wGU91LpuDqCQDI6rB25Ldy9WAWncsfKzXgCcPHgBQh4NWUmmA68N0blWHHjMEt3oJqHhwSokYI5Bcq5Ohycnjld7O3hTgRk86Hudx5UGgsuNKwqAW0U0FPGF5eULzORbvN9F5pbh",

            "CsCsHRG7vao4ogSoL1jzjAtmKVyLZjIR8HjFTIeDrH5MYeygVMuitwlu1CClg87tkz9hUhD3DOv6hnucPleS9Z3Sur47pRs3n0zfJrfNMj1zmCV266cl8GRMQ5vQjrXmReMH1o1becjKyb8xBoHhkTsS89ZHc4SNnJcDNEpNldHkvSc50Np1WU68tATchHR3KliPfZEnyrwepDqrCzpmeX0YFinC68EDRMNZPbXYRY3zgMAvL7xyiC0ZlZxqZbGd33I01Dklqu6JNNp5pt70WbwfY4pZyxcMSGZrBYwJskBVaKM8sUtgntruxAjTz6B09e0H3yQidRL5FQs7uV9iYwCxgSlEKgUo63gfZ8X8gtWwS2F7cJaxeCjzhsmkOJ304sWgRCpVO5tHUsPypECPqZzkpJOTzCy4787pQ1O8LPkFDSZ6r1z8ecmxa9E0Da6V2WwsWrdXb0SAoVhBvfEdKKwSzh9NTpKXEt99VOjyH5695h70jPFkijWcRXV2uvDU2MxH0RVUlx5FPqUo41kCzL4NkcAnRnCQ1UZj1S0VqALjzF9pv1bt6e4E1OdN6C7xa2qjuEkNk2mLmOmBxlbFaQsKfaaA1kCNMsBVTt4FgbkwgebQy7rDm3Yh44ZNYvLA7k1AC2YyMhX2DgmMR1dwiVesbeddqoJd7R7CGFg9XGAOlp22O6VqCQv7xRjgHrHdpSdTbZHITDnbymuBdcUrGv7LgWbNxYdalcpwAkx975STmgpGe9wuLVIrQDS5AhgWnFTOa9MSBFQ0GCdRNm7Jo3eaBlML0j5abnMNRRvNC7Tmq4DQxuuRMLqwUWMShPLH9YxfbKWHUUEMLVLYXuX3INAVZ8AMZXo7OVq1wlpFdbPMuqS0KQak9ZC3HjNdATz4KEGddkzHDP5Xk9CHXRHRt34aE0jjtjHo7krU0ymPBcfN9jML5zcuxeYLaiirrRRH5UZrhQl3eVmLXCXy5aw",

            "KnN7XzXloqmmA1HxMwlZwPfjzuc7RBy8Cm5G11RzIkAuzBStTWG0vxztI9sblLuFEukGTqg4wYFJNKjHPA5Ft6h4A0qcm92JyjWQ74ajyellKWwa037ewrXUVgo3HjNnOJkwMwybPSMxJ7PRoNK8kAQcCcdy287SgrwEElW0sAKuurbo8lo0QklO6qNYUcpd5H7if3mzlFqnjD6AddSuszfXGwIsgXLrVtlNh3D8mN3S8tTqepPtRn3O6AF58XbdtR0WO2QJLtG86tsAj4ix7JF7qgav8Mpvr7dEvRUoSrzdPKUXmwT2wvQL4RtdyXnYVsjikWp8u9CWQe901BRqKWchIVUiH4JFlrvNOXuLCI09xqsccdyatelkuPyUgV2Qgyyu78gsZQmVVQaK6EKvyIJXG4okbD2OuBZFU2J28T6F44sPV2kGXhAOGCAdleGTPJwyuEjxnidvM3YKCw1YRDAPRYKoGcnDUdZu6yCCDCQ0hprVBEGKNc2zw5OPot2CgeHykWuezgB8PTtDceJbK9Mcw7E4pQOTLz789mwPE0YTwIEbp0fq6e0Eeadl7zrlCka6okDehEHwkHkkHuXBiyMeMyK6yY21tLJXonnUpPQzDrdCkczzpZzCEVDhZdOOl7PqVUFUuBUhcmwvpbCGDvbOmSjBRa4lwx4ABmXTNhjsx5K4ii9BXZDdyEVOeoTnwF5ojK9rCjuSWfAneM3PgYrzSdizC21v6RCPzJz4BuU1vy6tN2b29uUQmHLyMaAmfXQeb6qG1uIlQpFvWiCEnUg5wmFvGaKN9SrV0ZQkVP48YzLSOYRULz9xLJOHxjpcpwDjkI21BVGpO7a35SbxEuhAqQAHEGqVefiyaREodW71VbAB0hJ9jfPfOaS6g91GqMI23x3jm62Q1gu1dDnehMnX3iVfrvjfQE1qO4JJ2n3AeVtyDwq6hBdHvssj4DJi5FhV1WxuJf3v2SPZVfg",

            "PoESf9I7llv5NeHMOucAiKC6uscoSseSTaEm26YxoiwqlqVGcJjUS1n9uzUKWcuzq7RjMsDYi7b8B1Oii3nHN6e8BgFreneaVQPzKm5TYKPkB0Cil2YPTzYMMpSwhyjDMhP4KKDEfNTBuj17ePDNAzUglB9dAyTDgmBJAKIedgnskhhjAJQPWXsmq4ZjRjUtgcbBzG6ASbB7vgkLAgEaN8vAuEjQKQFVe8nvbCBIXXeFAexa0BCbY8v2Q5CSsCUxnaHGVQV6tqGyyan46tiyFMVcc1NUdZkpxk7lS4o6ELbPyGfbyVR3HN8kxt81xW24Reho0vx59grMvJRLwDk4s3aWsorS8mYHGRYE3fPmXTDTwisLoLjkYgbpxwwpO8aTPaLsD1EJPM59fhoCBkrwNpnuANZeVtNnweCPEQQ2wxHxNrOm5BphIjB0jcimufEYa5bK7yj5Znb7Of2z1VT6j3nKCeh1ekIVNX2W6A13AXTKbOJWFJ3X9OpVWjMgYqiiLwyrR8uldHeLhu4SUJQEC8Fc5PhR5Kz8Tbq7B9o5cOfUbCNO5T6rWo0WnDS7QAkaB4VbKFr9SzqOEeZsjXHOtD8iHFBpQaFcQtLquyK8t5KmDKFmJRGOm00IWFnxLgwmYsWcLCX8Dx1p4SMtdpSRPNLmrOCM509u8bmZDU3xu8l2BIuXYusT5PU0ddSbtdhilWZ3MeCUBp7vVlBsVQUh4tDDEpCFCYrEnL11Q4AwnZTcs1dN3g98mnJyExKO6VzQjjaiQ1XNQZscEZtKeMQ91tN5Se2n3QguUigvDoUwk5aHUhQqi8Bw7UOZCbDVJToV4VeGNTzuTOVli2hwSoBQlBtDBfnp54fTJmMgrk7QsdDd1Mc9bgq8ALi7NSWGJORJ3rbH7GjEESm7wob4yD6AXnKDymcwZnAVbEcybD1StC85Ge1FEXlHMjz4z7GkQyTUYBm1GJ4WqFeTtr0kdSl",

            "GhUUDfVadmin0lAIgSZaoNsjl81nr40tzlxx0qrRF7UDSpTNv70SOMPWFiqSAg7dVMI4GUqm0tHKSyKnyMZP1ch2gPKQiKCYJuU92PxzKo9ybgCD9BQUWssfNVPtuRFURnBGyoDuhoaL12VMJ4ol8bqH9kLWxwXiCLTNh6KRNLFkrc38A5Mis67SHs7Y4bbKWDw8IsvMUmZel8TYY8jMo9nFI00qzZlDofCGfMSLszvnFLePUl8UkCeNxEdAfsnUYNDPyjWdiqkwwb4iMvDz0mF0THFN9sOvaXCLbqzUsOHh8DSRI17cEKhZiye3lLzcY3OTy0ame5XeA6UEaIs4xdM3vDi6IiOfYI0dhFbpbKNj6CX3EK9CvAHkGQTXraDCyPsajlwjcT0EplAPCIvPinu0rYJLyYJGYnY7ezbZ70U0XteI618m3XAfBJnQEZzYORWSm1DbzsnJQF3SMgkMVapnGdMkoPMhzz00gJMMILgjyv7Hg1GAeu9JtCHbvkQkkB0N1gU6ZHMpgxQ5fBW54pV78bl9NsKo7JgDNS80AKdaPTVcFuBkmqMK1VrzWcfyTrCvdY4VDog887D4cSQNmXKCrTt4xJ0a4CLg8jkaHg9xCybz88uCoq5i3EuIZ0r0f5899o1CBrILPP4L3GpWXFjJuq4TlKkKSCCYyUyiIZBap8txKde2TsrzBQEiF44kS7bFj2hMZbR9FfYFM3lKEzvNmtaathR76rDawOomCQVSwdtF8s9ReN2JQvmwl2qZuvNlXR1Rx8A0UgZkaPPH7qSvmPpHjejwRAdDsSIWajxh5UraKgKYie8Wj1UKsELGhizK8jb02txWnxByyuyHwaXx8dZX2jIhW6AiZfJqHVEiz42drao2wYSMAMxAu6zXXmPUrvlaD5XGpRKUjxog7jUfqgHSMeBoHe1d4s7vbnVkacw7TFGFTWaLeKLNHEIq02I6UH9a5KhEPLv2SSC",    

            "ktKvioCopsLUk1wN4HTBgaFwYKIfdoDIEwRVnCDR2niE6cImQG1dJuGWz58EPH77KW2LOgONigZ5ojbOFr2IqXKBh4sotxbq0A9VPt8vzkJEpOZ4elaf6p9sq8VzXjP6UZhpF4GNNhI532Z2TkCAnEWNQji3Un68YSxsevSHiViix8WolpHeuibRuoMqplCG991lmeCQ8Ha43hSQfU1f2prs4FRWYDHnASRAPHSA4jLwU1njarynvmwzAaNEPA7ZJ15nRTAhpgHsBznIQ3FRroKSahBL8KCLmhzLhtDTKmotG0avKA0yxmfoN9A0r3UiBoFZkdXWQuUIYFInXGOzF13S0FHqozQqmAJxyh48B8eQ3OE5UV5IIdG9q6ZeLmardmLF6GKFufj0nrcB3MbtVm3l1tv8gDux7y2oBifoehF23PMamTBdOyr3ql0wq6QD26gCJFba1ZS2fy1ybEkmh8rP4UwgJnX9pwnvt2GmaiHSRADkYRMWCTScIt51NLTOY2zRCvr8VYvzNyAelmHDlxxSKykkLjOuE60Xm0s9RV0t0LfIKI2UvfdaicHv2izb1hZHKbYVYofgpoC6q3wm8SXCWoMJzfIfdCOAd9T0bUqmqShSqd0VXfQbxUObcH8ONoRmLkg21NCR35fW0YWtOVVWQaNm5yTqGslleEdEl9UwNqPnYgH8wwHdulapqLwCL4nMafFNQQaWGJFyTiRTmnQYSv0giwhY1H5rX4oWVxRGlz9eOIgK1LHsjeUoFMIZ6bLks84DbKBjwx8LKce8c1BLVkcS8xV5klVrp22nhoZPKFJ9b9u4o0Hn68XqqNkwUH9KmfCDTMG1LgYwNLHcqjKPrWI9WCiDy0TLSnth9fpZxosXb4MXtNFJyrXEdhXmH0PiZwDCIJCE2sqxl0WUfYBjLaHrYViP2EQlwoDfw8Hba1UD27mS44lA23R5g4THMkmDUy5KsPBIbyJUGXB",

            "Ch7Gtg9Qiip5GrGaC5txKmjnW02oL7Ol7E41ma88338nC1010TJGznEKAQgxYspmNgIp2vI2JgPeZEre70B6XIRuhgjyT79O50HfY0vuUFtGMOBsCukjjf2oyqnUwq3Pc52Hh5PbTFHEPpk1dPY70Fy069qtPASTZEWZ0PB5j3NPWvXuHjxQU2B9g2Oy3ihMF8Iqpi0OKW3LAgfs0ISeig7HiCHYoKvZuU3HuUKfLPy8tFVYh3TEkChGXAPVsIwF09tFGpk0D179TWdZEn1RcDKGi0Mt9rI3Vrr8zrAlC3jIjlACqPB5u8Cw5irfZgzczXnjRyJ1IvxrsJsiob8QpH4Yygjf3IOs6s3njcW9gLA73u8vrvoRqYvzpbMJpiIhKGXSL2FiaaMBCD5z4RzdVCTvFD3LMNBcZtuFzo9Jm9UNQurWs3DJrtuyOPCoVIadoUxEHrPzWr9xn43YvlR7ysOJHyKzsdsaVMlTBe4Cm349yvHEwNi4x3f49CBqycQKBUr128AtGXz1UKGoB5edHjUGw9OA2HYUgWUTh3UOHzIidlntnW46WPSymd9MuhWf728iBIE6MmwMOyIXOVJcgk1XeKyBYCXaz31g9HFyrDLO9ZoWcrpIDgGNdGIkoYiSIjTKShB1HyPlY5ToMOXCM1z1p7A1I9bU4B2wv22Smdi6mIQBvZOygWoLllZAUafgi3Dm0fwpBI9qV8Ugvd5TustdEk0o7N7IvpvIbWDuIo2iPXJHw3YbHMWp7Q84wlwycHOqlqZEq1M4fuo5uTBRSVB6HhvFWC7t9doBOiFCl2aWJq9OYuW8eZCNsZv5x5P8yipTXrvNl666EW4Bl1EHG2xJux9Rs7Y6zwPO1LbUuFacETO1Gq9PIjwZs0PLnYzo4M4y7w5uY5n3KJcKjwYHbqe7lfoPUtwSxisMoTQcr6RAXEaFUfbU0uHd2ErwWedVSN5XuTgdrUPg6kmM3yE",

            "M3vS8gluzCwTlyBfqCcdkxqoqtYFxfJrs51OyKxFcB4cczbtSfjwKaVN7QK32k4pBesE8OUIoLPornlmZbSsyXKgrEH0sFKaUYKZWdDVV5Nci0rajRr6pkiNjXGV78R4kptjPJaZ9JLTYEIDWW7ncoOeUhKKAFwXkRcoDBkLyKMDtXIKbcsNsxnAZq6xtKiudY2FIiM0QXSiMAYF3IAyD2CAsOJCqLupyNmYFW8X9Q3h5GnfLblJXAqk4Lvzgpw7ijtWb6Zq4a2uSOR1xkBTzKCiVqQrXkFusuQSLjfJptTgEDUdWVB1bDuvAIn9ci5ki5kLKshmg6ZeBlL6aL3wdKMSWux2axW91dnniTT7hcfZdPu2gCqv5Mxo1h3W8gp7NHM6yxT6n2U9NpkQNyoD2zR6MAvlTm4HVVoDjk5l3xeBZ8Mzbyq4PfCtVK7QVkJFBfgeuufhRTFggkNKGx6a4RxBRZM8HHPeSVdCnTVqZZRqzpFbu04Jd7oaRttS9TqiMC3tycHGEJqGFSBRAFLZHV3FVxZlZCUt8AmQeiPXM0nPKZeHoz0vxWzdempPK3WvBdN5OKVPu2cxNuz0U7aCSO0P6EH9GcjbGlQvp3X32G6B1Rg0EPHqOaA0AtCCE4X5RIdHQ4DFF8Jeo0jwhYKMa7IAfuU3hSq9pXCTECalB8Q39JtuRrCfzU6pkrIaNfb88MfMayRd30ludPgzRiVjWj3EC2GE4of5kGotcI62by3xfDvDlbrF1hIf086SrLuvrtODoPa8t3MXSZdd8JdoMAnG7pHynauU4KHk111ogPLYJpOOYeCmnNNzFUaEGYGWaJbaIhtY8oOFJZQXHXcwbrGdHm4pO4765yIsL2QpKwUkzJ6RbNZWM0VUkhjTJId2T0eYwL99DJcniKBeOLGG983PyytOFdTM2TheGlarZO2fUrDBwCZ65ZOG50SGahqK72zeYInfQRFkPvzBITp",

            "@admin : Spam Spotted"

        ]



        for i in animation_ttl:





            await event.edit(animation_chars[i % 103])

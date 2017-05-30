from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_start(self, update):
        text = update.message.text
        return text.lower() == '0'

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '4'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '5'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '6'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '7'

    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '8'

    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '9'

    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == '10'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == '11'

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '12'

    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == '13'

    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == '14'

    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == '15'

    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == '16'

    def is_going_to_state17(self, update):
        text = update.message.text
        return text.lower() == '17'

    def is_going_to_state18(self, update):
        text = update.message.text
        return text.lower() == '18'

    def is_going_to_state19(self, update):
        text = update.message.text
        return text.lower() == '19'

    def is_going_to_state20(self, update):
        text = update.message.text
        return text.lower() == '20'

    def on_enter_start(self, update):
        update.message.reply_text("作業看累了嗎？歡迎來到輕鬆der心理測驗~這個測驗將會告訴你跟哪一類型的創業家最像哦^^\n（e.g.如下題，若選擇飛天則直接輸入'1'）\n飛天、隱形和讀心術會選哪一項\n1. 飛天\n2. 隱形\n3. 讀心術")

    def on_enter_state1(self, update):
        update.message.reply_text("既然計劃趕不上變化，那幹嘛要計劃\n4. 不怕一萬，只怕萬一\n5. 就隨機應變吧")

    def on_enter_state2(self, update):
        update.message.reply_text("看到電視節目介紹好吃的餐廳，會馬上搜尋\n5. Yes!\n6. No!")

    def on_enter_state3(self, update):
        update.message.reply_text("聽到朋友說自己是外星人時的反應\n6. 對R，I came from Mars.\n7. 逆才4咧")

    def on_enter_state4(self, update):
        update.message.reply_text("可一個人帶隨身行李就出門旅行兩三天\n8. 天地為家，雲遊四方\n9. 一個人...人家才不敢捏><")

    def on_enter_state5(self, update):
        update.message.reply_text("專心起來會廢寢忘食\n8. 咦天亮了！？\n10. Zzz...")

    def on_enter_state6(self, update):
        update.message.reply_text("每天花在電腦上做課外活動的時間超過3小時\n9. Yes!\n11. No!")

    def on_enter_state7(self, update):
        update.message.reply_text("看到人群圍觀就想參一腳\n10. What's happened?\n11. 人好多=  =")

    def on_enter_state8(self, update):
        update.message.reply_text("在公車遇見名人會\n12. 上去搭訕人家>////<\n13. 怕.jpg")

    def on_enter_state9(self, update):
        update.message.reply_text("參加比賽贏了之後會\n12. 和人分享\n13. 偶超低調")

    def on_enter_state10(self, update):
        update.message.reply_text("非常愛問5W1H\n12. 為什麼~為什麼為什麼！\n14. 還是問天吧")

    def on_enter_state11(self, update):
        update.message.reply_text("路上遇到不熟的朋友\n13. HI~~~~~\n14. （飄）")

    def on_enter_state12(self, update):
        update.message.reply_text("你想去哪兒\n15. 我只想在家\n16. 金銀島\n18. 夢幻島")

    def on_enter_state13(self, update):
        update.message.reply_text("看到路邊的阿婆賣花\n15. 人都有惻隱之心\n16. 會有人跟他們買吧~\n19. 老人詐騙集團？")

    def on_enter_state14(self, update):
        update.message.reply_text("看到中意的手工產品\n16. 看別家店有沒有比較便宜\n17. 自己DIY\n20. 買下它")

    def on_enter_state15(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...嚴長壽型！\n你具有悲天憫人的偉大情操，創業之後懂得將自己的成功回饋社會。\npress 0 to restart...")

    def on_enter_state16(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...Mark Elliot Zuckerberg！\n你具有國際化的眼光，並且對跨國創業有濃厚興趣。\npress 0 to restart...")

    def on_enter_state17(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...戴勝益型！\n你是個談笑風生的人，喜歡與人交際，並擅長鼓勵他人。\npress 0 to restart...")

    def on_enter_state18(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...林懷民型！\n你對於藝術與文化有自己獨特的想法，夢想走出自己的一片天。\npress 0 to restart...")

    def on_enter_state19(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...Steve Jobs！\n你有著強烈企圖心與勇氣，不畏怯前方任何困難，勇於實踐夢想。\npress 0 to restart...")

    def on_enter_state20(self, update):
        update.message.reply_text("恭喜完成作答^^測驗結果為...王永慶型！\n你有著不凡的器度與當大老闆的潛質，未來前途無量啊。\npress 0 to restart...")


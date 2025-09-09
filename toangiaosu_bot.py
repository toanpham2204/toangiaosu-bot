from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re
import os

TOKEN = os.getenv("TOKEN")  # lấy từ biến môi trường khi deploy


# Ý nghĩa Năm cá nhân
Y_NGHIA = {
    1: "🌱 Năm cá nhân số 1 trong Thần số học được xem là biểu tượng của sự khởi đầu mạnh mẽ, đánh dấu chu kỳ mới trong hành trình phát triển cá nhân. Đây là giai đoạn lý tưởng để bạn bước ra khỏi vùng an toàn, xác lập mục tiêu mới và xây dựng lối sống tích cực, đầy kỷ luật.

Số 1 trong năm cá nhân mang năng lượng tiên phong, thôi thúc bạn trở nên độc lập hơn, tự tin hơn và sẵn sàng chịu trách nhiệm cho con đường mình chọn. Những thói quen cũ, lối tư duy trì trệ cần được thay thế bằng một tinh thần hành động, sáng tạo và đổi mới.

Đặc biệt, với những người mang số chủ đạo 10, năm cá nhân số 1 có thể đem lại nhiều cơ hội phát triển đột phá cả về sự nghiệp lẫn tài chính. Tuy nhiên, chính sự thuận lợi này lại có thể khiến bạn chủ quan và dễ rơi vào trạng thái mất cảnh giác – đặc biệt trong lĩnh vực tiền bạc. Số 1 trong năm cá nhân cũng có thể “kích hoạt” lòng kiêu hãnh, nếu bạn không kiểm soát tốt bản ngã cá nhân.

Để tận dụng tối đa năng lượng từ năm cá nhân số 1, bạn cần học cách làm chủ chính mình – từ suy nghĩ đến hành động. Đây là thời điểm lý tưởng để bạn tập trung vào mục tiêu dài hạn, khởi xướng các dự án cá nhân và khẳng định bản thân trong cộng đồng. Hãy nhớ rằng, sự ủng hộ từ những người xung quanh là nền tảng giúp bạn phát triển không chỉ về vật chất mà còn cả tinh thần.

Năm cá nhân số 1, số 3, số 5 và số 8: Đây là nhóm cộng hưởng mạnh mẽ với năng lượng của năm thế giới số 1. Bạn nên chủ động nắm bắt cơ hội, mạnh dạn đổi mới, thử nghiệm và kiên trì theo đuổi những kế hoạch dài hạn. Năm 2026 sẽ mở ra nhiều cơ hội đột phá, giúp bạn tiến nhanh hơn trên con đường thành công.",
    2: "🤝 Năm cá nhân số 2 trong Thần số học tuy không mang sức mạnh bùng nổ như năm cá nhân số 1, nhưng lại nổi bật với năng lượng nhẹ nhàng, êm dịu và đầy chiều sâu. Đây là năm của sự bình ổn cảm xúc, rèn luyện sự kiên nhẫn và hướng đến những kết nối tinh tế trong đời sống nội tâm.

Trong số 2 của năm cá nhân, con người thường có xu hướng nhạy cảm hơn, thấu cảm hơn và dễ cảm nhận được chiều sâu tâm hồn – cả của bản thân và người khác. Đây không phải là thời điểm lý tưởng để đưa ra các quyết định lớn hay thay đổi đột phá, mà là giai đoạn để bạn nuôi dưỡng sự cân bằng, xây dựng các mối quan hệ vững chắc và phát triển nhận thức tâm linh.

Năm cá nhân số 2 cũng là thời gian tuyệt vời để lắng nghe trực giác, thực hành thiền định, kết nối với bản thân ở cấp độ sâu sắc hơn. Những ai đang theo đuổi các giá trị tinh thần, chữa lành và hòa hợp nội tâm sẽ tìm thấy nhiều bài học quý giá trong năm này.

Đặc biệt, năng lượng của số 2 trong năm cá nhân có tác động rõ rệt với những người mang số chủ đạo là 2 và 11 – những con số vốn đã nhạy bén và giàu cảm xúc. Năm nay sẽ là cơ hội để họ học cách tin tưởng vào dòng chảy tự nhiên của cuộc sống, phát triển sự kiên nhẫn và hướng đến sự hài hòa toàn diện trong tâm hồn.

Năm cá nhân số 2 và số 6: Hãy ưu tiên sự cân bằng trong các mối quan hệ, cũng như phát triển nội lực một cách hài hòa. Tập trung vào việc kết nối, hỗ trợ và làm việc nhóm sẽ giúp bạn gặt hái thành công bền vững trong năm cá nhân 2026.",
    3: "🎨 Năm cá nhân số 3 trong Thần số học là biểu tượng của sự phát triển trí tuệ, sáng tạo và khả năng giao tiếp vượt trội. Đây là giai đoạn mà sức mạnh tinh thần và tư duy của mỗi cá nhân được khơi dậy mạnh mẽ, giúp bạn thể hiện bản thân một cách tự nhiên và thu hút.

Dưới tác động của năng lượng số 3 trong năm cá nhân, bạn sẽ cảm thấy tinh thần phấn chấn, dễ mở lòng và sẵn sàng thử nghiệm những điều mới mẻ. Đây là thời điểm lý tưởng để theo đuổi các hoạt động liên quan đến nghệ thuật, viết lách, diễn thuyết hoặc bất kỳ lĩnh vực nào cần đến óc sáng tạo và khả năng truyền cảm hứng.

Năm cá nhân số 3 đặc biệt phù hợp với những người có số chủ đạo là 3. Sự cộng hưởng này giúp họ phát huy tối đa khả năng quan sát, tư duy nhạy bén và tinh thần lạc quan vốn có. Khi đón nhận năm này với tâm thế cởi mở, họ sẽ có nhiều cơ hội mở rộng các mối quan hệ xã hội, phát triển kỹ năng cá nhân và tạo nên bước ngoặt trong hành trình phát triển bản thân.

Năm cá nhân số 1, số 3, số 5 và số 8: Đây là nhóm cộng hưởng mạnh mẽ với năng lượng của năm thế giới số 1. Bạn nên chủ động nắm bắt cơ hội, mạnh dạn đổi mới, thử nghiệm và kiên trì theo đuổi những kế hoạch dài hạn. Năm 2026 sẽ mở ra nhiều cơ hội đột phá, giúp bạn tiến nhanh hơn trên con đường thành công.",
    4: "⚒️ Năm cá nhân số 4 trong Thần số học được xem là giai đoạn để bạn tập trung vào việc củng cố nội lực, xây dựng sự ổn định và tổ chức lại cuộc sống. Đây không phải là năm của sự bùng nổ, mà là năm của kỷ luật, sự kiên trì và lập kế hoạch dài hạn.

Trong năm cá nhân số 4, mọi khía cạnh của cuộc sống đều cần được xem xét một cách nghiêm túc. Những điều không còn phù hợp, không mang lại lợi ích lâu dài sẽ cần được loại bỏ, nhường chỗ cho các giá trị thực tiễn và bền vững.

Thần số học số 4 trong năm cá nhân đại diện cho việc thiết lập trật tự và rèn luyện bản thân. Đây là năm lý tưởng để bạn chăm sóc cơ thể, thiết lập lại lối sống khoa học và tập trung vào mục tiêu cụ thể. Việc tạo ra thói quen tích cực, giữ gìn sức khỏe thể chất và tinh thần chính là nền tảng giúp bạn tiến xa hơn trong các năm tiếp theo.

Năm cá nhân số 4 và số 7: Cần tập trung vào việc xây dựng nền tảng vững chắc. Hãy kiên định, kỷ luật và thận trọng trong từng bước đi. Mặc dù chưa phải là năm bứt phá mạnh, nhưng đây lại là giai đoạn quan trọng để tạo thế ổn định cho tương lai.",
    5: "🌍 Năm cá nhân số 5 trong Thần số học là giai đoạn đánh dấu sự chuyển mình mạnh mẽ, nơi mà khao khát tự do, trải nghiệm và sự đổi mới được thể hiện rõ nét. Đây cũng là thời điểm mà các yếu tố cảm xúc, tinh thần và tâm linh trỗi dậy mạnh mẽ hơn bao giờ hết.

Thần số học số 5 trong năm cá nhân tượng trưng cho sự linh hoạt, bứt phá khỏi khuôn khổ cũ và khám phá những hướng đi mới mẻ. Năng lượng của năm nay mang tính liên kết chặt chẽ với quá khứ (năm trước đó) và là tiền đề để phát triển sáng tạo cho năm tiếp theo.

Tuy nhiên, với những người đang trải nghiệm năm cá nhân số 5, điều quan trọng là hiểu rằng “tự do” không chỉ đơn thuần là sự giải phóng về mặt thể chất. Đôi khi, đó còn là sự tự do trong tư duy, trong cách nhìn nhận vấn đề, và khả năng làm chủ chính mình giữa những thay đổi nhanh chóng.

Năm cá nhân số 1, số 3, số 5 và số 8: Đây là nhóm cộng hưởng mạnh mẽ với năng lượng của năm thế giới số 1. Bạn nên chủ động nắm bắt cơ hội, mạnh dạn đổi mới, thử nghiệm và kiên trì theo đuổi những kế hoạch dài hạn. Năm 2026 sẽ mở ra nhiều cơ hội đột phá, giúp bạn tiến nhanh hơn trên con đường thành công.",
    6: "🏡 Năm cá nhân số 6 trong Thần số học được xem là giai đoạn của sự sáng tạo, chăm sóc và vun đắp các mối quan hệ cá nhân. Đây là thời điểm lý tưởng để bạn khởi xướng những dự án mang tính nghệ thuật, làm đẹp không gian sống hoặc nâng cao chất lượng đời sống tinh thần.

Nếu bạn biết cách tập trung vào những giá trị mang lại sự ổn định và hài hòa, thì năm cá nhân số 6 hứa hẹn sẽ mang lại nhiều thành tựu. Đặc biệt, Con số 6 trong năm cá nhân còn thể hiện trọng tâm của gia đình, sự gắn kết và tình cảm giữa các thành viên. Những hoạt động sáng tạo liên quan đến tổ ấm như trang trí nhà cửa, chăm sóc con cái, hoặc xây dựng một cuộc sống hài hòa đều được thúc đẩy mạnh mẽ.

Đây cũng là năm bạn nên dành thời gian quan tâm nhiều hơn đến những người thân yêu và nuôi dưỡng sự đồng cảm trong các mối quan hệ.

Năm cá nhân số 2 và số 6: Hãy ưu tiên sự cân bằng trong các mối quan hệ, cũng như phát triển nội lực một cách hài hòa. Tập trung vào việc kết nối, hỗ trợ và làm việc nhóm sẽ giúp bạn gặt hái thành công bền vững trong năm cá nhân 2026.",
    7: "🔮 Năm cá nhân số 7 trong Thần số học là năm của sự tập trung, chiêm nghiệm và vượt qua những chướng ngại vật bên trong. Đây không phải là thời điểm để mở rộng hay tạo ra những thay đổi lớn, mà là năm bạn cần dành cho mình sự tĩnh lặng để củng cố nội lực, khai thác chiều sâu của bản thân.

Số 7 trong năm cá nhân thường liên quan đến những bài học mang tính cá nhân và tâm linh. Trong giai đoạn này, bạn nên ưu tiên dành thời gian suy ngẫm, trau dồi kiến thức và phát triển trí tuệ nội tâm. Công việc đòi hỏi sự tập trung cao độ, vì vậy bạn cần rèn luyện tính kỷ luật và tránh xao nhãng bởi yếu tố bên ngoài.

Có thể nói, năm cá nhân số 7 là một năm thiết yếu để bạn học hỏi từ những trải nghiệm sâu sắc và trưởng thành hơn qua từng thử thách nội tại.

Năm cá nhân số 4 và số 7: Cần tập trung vào việc xây dựng nền tảng vững chắc. Hãy kiên định, kỷ luật và thận trọng trong từng bước đi. Mặc dù chưa phải là năm bứt phá mạnh, nhưng đây lại là giai đoạn quan trọng để tạo thế ổn định cho tương lai.",
    8: "💰 Năm cá nhân số 8 trong Thần số học được xem là năm của trí tuệ, sự độc lập và bứt phá mạnh mẽ. Đây là giai đoạn đánh dấu sự chuyển mình rõ rệt, khi con người không chỉ củng cố nội lực mà còn sẵn sàng vươn lên đỉnh cao trong cả sự nghiệp và tài chính.

Thần số học số 8 trong năm cá nhân tượng trưng cho sự trưởng thành, tư duy chiến lược và khả năng kiểm soát. Với nhiều người, đây chính là thời điểm thuận lợi để nâng cao năng lực lãnh đạo, gia tăng thu nhập và đạt được những bước tiến đáng kể trong công việc. Đồng thời, bạn cũng sẽ phát triển sự độc lập về mặt tinh thần, không còn phụ thuộc vào người khác như trước.

Tóm lại, năm cá nhân số 8 là một năm đầy tiềm năng cho những ai sẵn sàng hành động quyết liệt và dám nắm bắt cơ hội.

Năm cá nhân số 1, số 3, số 5 và số 8: Đây là nhóm cộng hưởng mạnh mẽ với năng lượng của năm thế giới số 1. Bạn nên chủ động nắm bắt cơ hội, mạnh dạn đổi mới, thử nghiệm và kiên trì theo đuổi những kế hoạch dài hạn. Năm 2026 sẽ mở ra nhiều cơ hội đột phá, giúp bạn tiến nhanh hơn trên con đường thành công.",
    9: "🌸 Năm cá nhân số 9 là thời điểm quan trọng, đánh dấu sự kết thúc của một chu kỳ 9 năm và mở ra những thay đổi sâu sắc trong cuộc sống. Đây là giai đoạn giúp bạn nhìn lại hành trình đã qua, đồng thời chuẩn bị tâm thế để bước sang một chu kỳ mới với định hướng rõ ràng hơn.

Dù những thay đổi vào giai đoạn số 9 trong năm cá nhân diễn ra tương đối âm thầm, nhưng chúng mang tính chuyển hóa mạnh mẽ từ bên trong. Nhiều người có thể không nhận ra ngay sự biến chuyển này cho đến khi bước vào những năm tiếp theo, lúc mà tác động của năm 9 bắt đầu bộc lộ rõ nét hơn.

Tóm lại, năm cá nhân số 9 là cơ hội để thanh lọc, buông bỏ những điều không còn phù hợp, từ đó tạo nền tảng vững chắc cho sự khởi đầu mới ở chu kỳ kế tiếp.

Năm cá nhân số 9: Đây là thời điểm kết thúc chu kỳ cũ. Hãy tập trung vào việc hoàn tất, buông bỏ và giải phóng những điều không còn phù hợp, từ đó sẵn sàng đón nhận hành trình mới trong chu kỳ 9 năm sắp tới."
}

# Hàm tính Năm cá nhân
def tinh_nam_ca_nhan(ngay, thang, nam_hien_tai):
    tong = sum(int(d) for d in str(ngay)) + sum(int(d) for d in str(thang)) + sum(int(d) for d in str(nam_hien_tai))
    while tong > 9:
        tong = sum(int(d) for d in str(tong))
    return tong

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xin chào! Tôi là bot tính Năm Cá nhân (Thần số học).\n"
        "👉 Nhập ngày sinh + năm hiện tại theo dạng:\n\n"
        "`DD/MM/YYYY NĂM`\n\n"
        "Ví dụ: `12/07/1990 2025`",
        parse_mode="Markdown"
    )

# Xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    match = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})\s+(\d{4})", text)
    if match:
        ngay, thang, nam_sinh, nam_hien_tai = map(int, match.groups())
        nam_cn = tinh_nam_ca_nhan(ngay, thang, nam_hien_tai)
        giai_thich = Y_NGHIA.get(nam_cn, "Không có dữ liệu.")
        await update.message.reply_text(
            f"📅 Năm cá nhân của bạn ({nam_hien_tai}) là: 🌟 {nam_cn}\n\n🔎 Ý nghĩa: {giai_thich}"
        )
    else:
        await update.message.reply_text("❌ Sai định dạng! Hãy nhập:\n\n12/07/1990 2025")

# Main
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()

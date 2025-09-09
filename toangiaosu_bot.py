from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # 🔑 Thay token của bạn

# Ý nghĩa Năm cá nhân
Y_NGHIA = {
    1: "🌱 Năm khởi đầu, cơ hội mới. Thời điểm để hành động, bắt đầu dự án hoặc mục tiêu mới.",
    2: "🤝 Năm hợp tác, kiên nhẫn. Nên tập trung xây dựng mối quan hệ và phát triển cảm xúc.",
    3: "🎨 Năm sáng tạo, giao tiếp. Cơ hội để tỏa sáng, phát triển sự tự tin và thể hiện bản thân.",
    4: "⚒️ Năm xây dựng, kỷ luật. Cần nỗ lực, kiên trì, đặt nền móng vững chắc cho tương lai.",
    5: "🌍 Năm thay đổi, tự do. Cơ hội du lịch, học hỏi, khám phá những điều mới.",
    6: "🏡 Năm gia đình, trách nhiệm. Thời điểm quan tâm đến các mối quan hệ và sự ổn định.",
    7: "🔮 Năm chiêm nghiệm, học hỏi. Tập trung phát triển tinh thần, trí tuệ và sự hiểu biết.",
    8: "💰 Năm thành tựu, tài chính. Cơ hội phát triển sự nghiệp, tài lộc và quyền lực.",
    9: "🌸 Năm kết thúc, giải phóng. Thời điểm buông bỏ cái cũ để chuẩn bị cho chu kỳ mới."
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

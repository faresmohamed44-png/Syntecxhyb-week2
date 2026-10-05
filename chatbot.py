import datetime
import re
import string

# قاعدة المعرفة المتقدمة للخدمات
knowledge_base = {
    r"\b(1|خدمات|خدماتكم|بتقدموا ايه)\b": 
        "نقدم باقة واسعة من الخدمات: 1. تطوير البرمجيات وحل المشاكل التقنية | 2. تصميم واجهات المستخدم | 3. بناء الشاتبوت الذكي.",
    
    r"\b(2|أسعار|الاسعار|تكلفة|بكام|كم سعر)\b": 
        "تختلف التكلفة بناءً على متطلبات مشروعك بدقة. هل ترغب في حجز استشارة مجانية لتقييم طلبك؟",
    
    r"\b(3|ساعات العمل|مواعيد|متى تفتحون)\b": 
        "نحن متواجدون وخدماتنا متاحة عبر النظام الآلي طوال أيام الأسبوع على مدار 24 ساعة.",
    
    r"\b(4|تواصل|رقم|اتصل|ايميل)\b": 
        "يمكنك التواصل معنا فوراً عبر البريد الإلكتروني الرسمي أو من خلال منصة المشروع.",
    
    r"\b(الوقت|الساعة|التاريخ|اليوم)\b": 
        f"التاريخ والوقت الحالي هو: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
}

default_response = "عذراً، لم أتمكن من فهم طلبك بدقة. هل يمكنك اختيار رقم من القائمة، أو كتابة (تواصل) لمعرفة طرق الاتصال بنا؟"

def clean_input(user_input):
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))
    return user_input.strip()

def get_bot_response(user_input):
    cleaned = clean_input(user_input)
    for pattern, response in knowledge_base.items():
        if re.search(pattern, cleaned, re.IGNORECASE):
            return response
    return default_response

def run_chatbot():
    print("==================================================")
    print("      نظام المساعد الذكي للأعمال (Commercial Bot)  ")
    print("==================================================")
    
    # 1. جمع بيانات العميل عند بدء المحادثة (Lead Capture)
    client_name = input("البوت: أهلاً بك! من فضلك أكتب اسمك الكريم لنبدأ: ").strip()
    if not client_name:
        client_name = "عميل مجهول"
        
    client_phone = input(f"البوت: أهلاً يا {client_name}! اكتب رقم هاتفك أو بريدك للتواصل معك لاحقاً: ").strip()
    if not client_phone:
        client_phone = "غير مسجل"

    # حفظ بيانات العميل في ملف Leads منفصل
    reg_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lead_record = f"[{reg_time}] الاسم: {client_name} | الوسيلة: {client_phone}\n"
    try:
        with open("leads.txt", "a", encoding="utf-8") as lead_file:
            lead_file.write(lead_record)
    except Exception as e:
        print(f"ملاحظة: تعذر حفظ بيانات العميل في ملف التصدير: {e}")

    # 2. عرض القائمة التفاعلية الرقمية
    print(f"\nمرحباً بك يا {client_name} في القائمة الرئيسية. يختار العميل الرقم المناسب للاستفسار:")
    print("  [1] الاستفسار عن الخدمات")
    print("  [2] معرفة الأسعار والتكلفة")
    print("  [3] ساعات العمل")
    print("  [4] معلومات التواصل والدعم")
    print("اكتب 'خروج' لإنهاء المحادثة في أي وقت.\n")
    
    message_count = 0
    
    while True:
        user_input = input(f"{client_name}: ").strip()
        
        if user_input.lower() in ["خروج", "exit", "quit"]:
            print(f"\n[إحصائيات الجلسة]: شكراً لك يا {client_name}. تم تبادل {message_count} رسالة.")
            print("البوت: مع السلامة! نتمنى لك يوماً سعيداً.")
            break
            
        if not user_input:
            continue
            
        message_count += 1
        response = get_bot_response(user_input)
        print(f"البوت: {response}")
        
        # 3. توثيق السجل العام للمحادثة
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] العميل ({client_name}): {user_input} | البوت: {response}\n"
        
        try:
            with open("chat_history.txt", "a", encoding="utf-8") as log_file:
                log_file.write(log_entry)
        except Exception as e:
            print(f"حدث خطأ أثناء حفظ السجل: {e}")

if __name__ == "__main__":
    run_chatbot()
    شكرا
    

مشروع تحليل بيانات العملاء وإيرادات المتجر (Customer & Sales Analytics)
وصف المشروع والبيانات
يقدم هذا المشروع تحليلاً متكاملاً لبيانات المبيعات وسلوك العملاء لمتجر إلكتروني بهدف تقديم رؤى استراتيجية تساعد الإدارة على اتخاذ قرارات مبنية على البيانات.

تم توسيع قاعدة البيانات التشغيلية (store.db) باستخدام SQLite لترتبط بجدول العملاء (customers) وجدول المبيعات (sales) وجدول المنتجات (products). تتضمن البيانات السجلات الديموغرافية للعملاء، تواريخ التسجيل، وتفاصيل العمليات الشرائية (الكميات، الأسعار، التواريخ، والفئات).

أهم 5 أسئلة تحليلية تم الإجابة عليها
من هم العملاء الأكثر قيمة للمتجر (Top Spenders)؟

ما هي نسبة العملاء غير النشطين الذين سجلوا في النظام ولم يجروا أي عملية شراء؟

كيف يتوزع أداء الإيرادات عبر الفئات المختلفة للمنتجات والاتجاهات الشهرية؟

ما هي نسبة العملاء المتكررين (Repeat Customers) مقارنة بإجمالي قاعدة العملاء؟

كيف يختلف متوسط قيمة الطلب للفرد مقارنة بالمعدل العام للمتجر؟

أهم الرؤى الاستراتيجية (Insights)
تركيز الإيرادات (قاعدة 80/20): تشير البيانات إلى أن أعلى 20% من العملاء يساهمون بأكثر من 40% من إجمالي إيرادات المتجر، مما يعني أن استقرار الإيرادات يعتمد بشكل كبير على شريحة صغيرة من كبار المشتريين.

ضعف معدل تحويل التسجيل الأول: يوجد حوالي 13.3% من إجمالي العملاء المسجلين خاملون تماماً ولم يقوموا بإجراء أي عملية شراء منذ انضمامهم.

نمو قوي في القيمة الزمانية للعميل (LTV): أظهرت التحليلات أن العملاء المتكررين يشكلون 46.7% من إجمالي قاعدة العملاء، وهم المحرك الأساسي لاستدامة المبيعات الشهريّة.

تفاوت القوة الشرائية حسب الفئات: تنحصر المبيعات العالية في فئات محددة من المنتجات، بينما تعاني بعض الفئات من انخفاض معدل الدوران رغم وجود حركة تصفح عالية.

التوصيات العملية لصاحب المتجر
إطلاق برنامج ولاء مخصص (VIP Loyalty Program): نظرًا لأن 20% من العملاء يمثلون أكثر من 40% من الإيرادات، يُوصى بإنشاء برنامج مكافآت حصري يقدم خصومات مخصصة ودعمًا ذا أولوية للاحتفاظ بهذه الشريحة وتجهيز حملات إعادة استهداف لهم.

أتمتة حملات التنشيط (Welcome Campaigns): تحويل العملاء الخاملين إلى خيارات شرائية عبر إرسال كوبون خصم تلقائي (مثلاً 15% على الطلب الأول) خلال أول 7 أيام من تاريخ التسجيل لرفع معدل التحويل (Conversion Rate).

طريقة تشغيل المشروع (خطوة بخطوة)
1. المتطلبات الأساسية
تأكد من تثبيت بيئة Python 3.8+ والمكتبات المطلوبة عبر الأمر التالي:

Bash
pip install pandas matplotlib seaborn plotly openpyxl
2. إنشاء وتحديث قاعدة البيانات
قم بتشغيل سكربت إعداد البيانات لإنشاء قاعدة store.db وتعبئتها بالبيانات الاختبارية وتحديث الجداول:

Bash
python create_database.py
3. تنفيذ التحليل واستخراج التقارير
قم بتشغيل سكربت التحليل الرئيسي لتنفيذ استعلامات SQL، استخراج التقرير في Excel، وتوليد الرسمات البيانية:

Bash
python run_analysis.py
4. استعراض المخرجات
بعد انتهاء التشغيل، ستجد المخرجات التالية في مجلد المشروع:

customer_analysis_report.xlsx: التقرير الشامل المنسق والمقسم على عدة صفحات.

chart_*.png: الرسمات البيانية الثابتة الخاصة بالاتجاهات والأداء.

chart_signup_vs_spending_interactive.html: الرسم التفاعلي لتحليل سلوك الإنفاق.

Customer & Sales Analytics Project
Project Overview and Data Description
This project provides a comprehensive analysis of sales data and customer behavior for an e-commerce store to deliver strategic insights that help management make data-driven decisions.

The operational database (store.db) was expanded using SQLite to link the customers, sales, and products tables. The dataset includes customer demographic records, registration dates, and transaction details (quantities, prices, dates, and categories).

Top 5 Analytical Questions Addressed
Who are the highest-value customers for the store (Top Spenders)?

What percentage of registered customers are inactive and have never made a purchase?

How is revenue performance distributed across product categories and monthly trends?

What is the proportion of repeat customers compared to the overall customer base?

How does individual average order value compare to the overall store average?

Key Strategic Insights
Revenue Concentration (80/20 Rule): Data indicates that the top 20% of customers contribute to over 40% of total store revenue, showing that revenue stability heavily relies on a small segment of high spenders.

Low Initial Registration Conversion Rate: Approximately 13.3% of total registered customers remain completely inactive, having made zero purchases since joining.

Strong Customer Lifetime Value (LTV) Growth: Analysis shows that repeat customers account for 46.7% of the total customer base, acting as the primary driver for monthly sales sustainability.

Purchasing Power Disparity Across Categories: High sales are concentrated in specific product categories, whereas other categories experience lower turnover rates despite high traffic.

Actionable Recommendations for Store Owner
Launch a VIP Loyalty Program: Given that 20% of customers generate over 40% of revenue, it is recommended to establish an exclusive rewards program with personalized discounts and priority support to retain this high-value segment.

Automate Activation Campaigns: Convert inactive customers into active buyers by automatically sending a discount code (e.g., 15% off the first order) within the first 7 days of registration to boost conversion rates.

How to Run the Project (Step-by-Step)
1. Prerequisites & Dependencies
Ensure Python 3.8+ and the required libraries are installed using the following command:

Bash
pip install pandas matplotlib seaborn plotly openpyxl
2. Database Initialization & Update
Run the data setup script to create store.db, populate it with test data, and update the schema:

Bash
python create_database.py
3. Execute Analysis & Generate Reports
Run the main analysis script to execute SQL queries, export the formatted Excel report, and generate visual charts:

Bash
python run_analysis.py
4. Review Project Outputs
Upon successful execution, the following output files will be generated in the project directory:

customer_analysis_report.xlsx: A comprehensive, multi-tab formatted report.

chart_*.png: Static visualization charts highlighting sales trends and performance.

chart_signup_vs_spending_interactive.html: An interactive visualization analyzing spending behavior relative to registration dates.
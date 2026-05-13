Reminder
========

Phần mềm chạy ngầm hỗ trợ nhắc nhở Check-in/Check-out và bảo vệ sức khỏe (mắt & cột sống) dành riêng cho dân kỹ thuật.

Tính năng nổi bật
-----------------

*   **⏰ Nhắc nhở chấm công:** Tự động gửi thông báo nhắc Check-in (trước 07:40) và Check-out (sau 17:30) từ Thứ 2 đến Thứ 7.
    
*   **👀 Bảo vệ mắt & Cột sống:** Tự động mờ màn hình (Dim screen) và phát âm thanh nhắc nhở vận động sau mỗi $X$ phút làm việc tập trung.
    
*   **⚙️ Giao diện tùy biến:** UI trực quan để cấu hình thời gian, tần suất nghỉ ngơi mà không cần sửa code.
    
*   **📥 Chạy ngầm (System Tray):** Thu nhỏ xuống khay hệ thống, không làm phiền không gian làm việc.
    
*   **♻️ Auto Startup:** Tùy chọn tự khởi động cùng Windows chỉ với một cú Click.
    
*   **🧪 Mode Test:** Hỗ trợ cờ --test để kiểm tra nhanh các tính năng thông báo và mờ màn hình.
    

Yêu cầu môi trường
------------------

*   **Ngôn ngữ:** Python 3.10+ (Khuyên dùng 3.14 như hiện tại).
    
*   **Hệ điều hành:** Windows 10/11.
    
*   Bashpip install win11toast schedule pystray Pillow
    

Hướng dẫn cài đặt & Sử dụng
---------------------------

### 1\. Chạy trực tiếp từ mã nguồn

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python reminder.py   `

### 2\. Kiểm tra nhanh (Test Mode)

Để kiểm tra xem thông báo và tính năng mờ màn hình có hoạt động chuẩn không:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python reminder.py --test   `

### 3\. Đóng gói thành file .exe

Sử dụng **PyInstaller** để tạo file thực thi độc lập (đảm bảo file logo.ico nằm cùng thư mục):

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pyinstaller --noconsole --onefile --add-data "logo.ico;." --icon="logo.ico" --name "reminder" reminder.py   `

Lưu ý quan trọng
----------------

*   **Antivirus:** Nếu Windows Defender nhận nhầm file .exe là virus (False Positive), hãy chọn **"Unblock"** trong Properties hoặc thêm file vào danh sách loại trừ (Exclusion).
    
*   **Startup:** Tính năng tự khởi động chỉ hoạt động khi bạn chạy ứng dụng dưới dạng file .exe.
    
*   **Icon:** Nếu không thấy icon dưới Tray, hãy đảm bảo file logo.ico được nhúng đúng qua tham số --add-data khi build.
    

Cấu trúc dự án
--------------

*   reminder.py: Mã nguồn chính của ứng dụng.
    
*   config.json: File lưu trữ cấu hình người dùng (tự sinh ra).
    
*   logo.ico: File icon của ứng dụng.
    
*   dist/: Thư mục chứa file .exe sau khi build.
    

**Developed by Thành Neee with ❤️**

_Vì một tương lai không quên quẹt thẻ và không bị thoát vị đĩa đệm._
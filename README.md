### SIMPLE BILLING SYSTEM

#### Overview
The Simple Billing System is a Python program designed to register products by scanning their QR codes using a laptop's in-built camera. It allows users to input the product name and price after scanning the QR code. All product information is stored in a text file named `Product_data.txt`. The program includes a sound alert feature using the `preferredsoundplayer` module, which plays a beep sound when a product is scanned.

#### Features
- Scan QR codes using the laptop's in-built camera.
- Register product information such as name and price.
- Store product data in a text file.
- Sound alert when a product is scanned.

#### Requirements
- Python 3.9.0 or greater
- `cv2` module for capturing images and processing QR codes.
- `preferredsoundplayer` module for playing sound alerts.

#### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kunal-kawate/SIMPLE_BILLING_SYSTEM.git
   ```
2. Install required modules:
   ```bash
   pip install cv2 preferredsoundplayer
   ```

#### Usage
1. Run the `Product_registration_sys.py` file.
2. When prompted, scan the QR code of the product using the laptop's camera.
3. Enter the product name and price.
4. The program will store the product information in the `Product_data.txt` file.
5. A beep sound will play to indicate successful scanning.

#### File Structure
- `Product_registration_sys.py`: Main Python program for product registration.
- `Product_data.txt`: Text file to store product information.
- `README.md`: Documentation file.
- `requirements.txt`: List of required modules.

#### Contributing
Contributions to enhance the Simple Billing System are welcome! Feel free to fork the repository, make changes, and submit a pull request.

#### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

#### Author
[Kunal Kawate](https://www.linkedin.com/in/kunal-kawate-%EA%AA%9C-168587229/)

#### Acknowledgments
- The `cv2` module for image processing.
- The `preferredsoundplayer` module for sound alerts.

#### Contact
For any inquiries or issues, please contact [kunalkawate424@gmail.com].

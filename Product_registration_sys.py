import cv2
import preferredsoundplayer as pr

def PlaySoundPositive():
    pr.soundplay("Beep-07a.mp3",1)

def PlaySoundNegative():
    pr.soundplay("beep-06.mp3",1)

def PlaySoundError():
    pr.soundplay("beep-03.mp3",1)

def main(Product_Ids,display_product_data):

    camera_id = 0
    delay = 1
    window_name = 'OpenCV QR Code Scanner'

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)
    with open('Product_data.txt','a+') as file:
        while True:
            try:
                ret, frame = cap.read()
                if ret:
                    ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
                    if ret_qr:
                        for s, p in zip(decoded_info, points):
                            if s:
                                if s not in Product_Ids:
                                    PlaySoundPositive()
                                    Product_Ids.append(s)
                                    print('Product ID: ',s,' Registered.....')
                                    product=[]
                                    display_product_data_Dicto={}
                                    Product_Name=input('Name: ')
                                    Product_Price=input('Price: ')
                                    product.append(int(s))
                                    display_product_data_Dicto['ID']=int(s)
                                    product.append(Product_Name)
                                    display_product_data_Dicto['Name']=Product_Name
                                    product.append(int(Product_Price))
                                    display_product_data_Dicto['Price']=int(Product_Price)
                                    display_product_data.append(display_product_data_Dicto)
                                    file.write(str(product))
                                    file.write('\n')
                                else:
                                    PlaySoundNegative()
                                    print("Product is already registered........")
                                color = (0, 255, 0)
                            else:
                                color = (0, 0, 255)
                            frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
                    cv2.imshow(window_name, frame)
                if cv2.waitKey(delay) & 0xFF == ord('q'):
                    break
            except :
                PlaySoundError()
                print('Please Scan code properly.......')
        cv2.destroyWindow(window_name)

def FileSetup():
    with open('Product_data.txt','w') as file:
        pass
    print('Product_data File created......')

def display(display_product_data):
    print('\n--------------- K SuperMarts LTD. -----------------')
    print('------------- Registered Products -----------------\n')
    count=0
    for item in display_product_data:
        count=count+1
        print('Product No.',count)
        print('ID:',item['ID'])
        print('Name:',item['Name'])
        print('Price:',item['Price'],'\n')
    print('Total Products Registered:',count)
    print('\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\- Thank You -//////////////////////')


if __name__=='__main__':
    Product_Ids=[]
    display_product_data=[]
    FileSetup()
    main(Product_Ids,display_product_data)
    display(display_product_data)
    

import cv2
import keyboard
import preferredsoundplayer as pr

def PlaySoundPositive():
    pr.soundplay("Beep-07a.mp3",1)

def PlaySoundNegative():
    pr.soundplay("beep-06.mp3",1)

def PlaySoundError():
    pr.soundplay("beep-03.mp3",1)

def PlaySoundPrinting():
    pr.soundplay("electric-drill-03.mp3",1)

def main(Product_data,Bill_products,regProIds,scanned_product_id):
    camera_id = 0
    delay = 1
    window_name = 'OpenCV QR Code Scanner'

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)

    while True:
        ret, frame = cap.read()         
        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        if int(s) in regProIds:
                            if int(s) not in scanned_product_id:
                                if(len(Product_data)!=0):
                                    scanned_product_id.append(int(s))
                                    print('Item ID: ',int(s),' Scanned Sucessfully.....')
                                    PlaySoundPositive()
                                    # ------------------
                                    for item in Product_data:
                                        if item['ID']==int(s):
                                            Bill_products.append(item)
                                            Product_data.remove(item)
                                    # -----------------------
                                    color = (0, 255, 0)
                                else:
                                    PlaySoundError()
                                    print("\nEmpty Product Data..........")
                                    color = (0, 255, 0)
                            else:
                                PlaySoundNegative()
                                print('Item already Scanned...................')
                                color = (0, 255, 0)
                        else:
                            PlaySoundNegative()
                            print("Unknown Product Found..............")
                            color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyWindow(window_name)

def readFile(regProIds):
    product_data=[]
    with open('Product_data.txt','r') as file:
        product_data_set =file.readlines()
        for product in product_data_set:
            single_product={}
            product=product.replace('[','')
            product=product.replace(']','')
            data = product.split(',')
            single_product['ID']=int(data[0])
            regProIds.append(int(data[0]))
            product_name=data[1]
            product_name=product_name.replace("'",'')
            product_name=product_name.replace("'",'')
            single_product['ProductName']=product_name
            single_product['ProductPrice']=int(data[2])
            product_data.append(single_product)
    return product_data

def DisplayBillProduct(Bill_products):
    count=0
    TotalPrice=0
    print('------------- K SuperMarts LTD. -----------------\n')
    if(len(Bill_products)==0):
        PlaySoundError()
        print("\nEmpty Product Data, plz check the Product data File..........")
    else:
        PlaySoundPrinting()
        for item in Bill_products:
            count=count+1
            TotalPrice+=item['ProductPrice']
            print('Item No.',count)
            print('ID:',item['ID'])
            print('Name:',item['ProductName'])
            print('Price:',item['ProductPrice'],'\n')
        print('Total Items:',count,' Total Price:',TotalPrice)
        Bill_products.clear()
    print('\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\- Thank You -//////////////////////')  

             
     

        
if __name__ =='__main__':

    scanned_product_id=[] #List for collecting ID's during scanning proccess of Items

    regProIds=[] # ID's of Registered Products
  
    Bill_products=[] # List for collecting scanned product data

    Product_data = readFile(regProIds) #Function which read data from the file

    condition = True
    while condition:
        print('------------- K SuperMarts LTD. -----------------\n')
        print('                Bill Gen. SYS.                   \n\n')
        print('1. Scan Products (Press Space) \n2. Gen. Bill(Press Tab)\n3. Exit SyS(Press ESC) \n\n')
        
        if keyboard.read_key() == 'space':
            print("\\\\\\\\\\\\\\\\\\\-Please Scan the Products-///////////////////////\n")
            main(Product_data,Bill_products,regProIds,scanned_product_id)
        elif keyboard.read_key() == 'tab':
            DisplayBillProduct(Bill_products) 
        elif keyboard.read_key() == 'esc':
            condition = False
            print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\- Thank You For Visiting -///////////////////////')

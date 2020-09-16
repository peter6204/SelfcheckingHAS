from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter

window=tkinter.Tk()
window.title("Self-Checking")
window.geometry("640x480+100+100")
window.resizable(False, False)

schoolname = str("하나고")     #학교이름 00고
studentname = str("홍길동")    #이름
studentnumber = str("030405")  #주민등록번호 앞자리(생년월일)


CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()
CheckVariety_3=tkinter.IntVar()
CheckVariety_4=tkinter.IntVar()
CheckVariety_5=tkinter.IntVar()
CheckVariety_6=tkinter.IntVar()


def A():
    c1 = CheckVariety_1.get()
    c2 = CheckVariety_2.get()
    c3 = CheckVariety_3.get()
    c4 = CheckVariety_4.get()
    c5 = CheckVariety_5.get()
    if c1 ==0 and c2==0 and c3 ==0 and c4 ==0 and c5 == 0 :
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        url = 'https://eduro.sen.go.kr/hcheck/index.jsp'
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        driver.find_elements_by_css_selector('.btn_confirm')[1].click()
        driver.find_element_by_css_selector('#schulNm').send_keys(schoolname)
        driver.find_element_by_css_selector('#schulNm').send_keys(Keys.ENTER)
        driver.find_element_by_css_selector('#pName').click()  
        driver.find_element_by_css_selector('#pName').send_keys(studentname)
        driver.find_element_by_css_selector('#frnoRidno').click() 
        driver.find_element_by_css_selector('#frnoRidno').send_keys(studentnumber)
        driver.find_element_by_css_selector('#btnConfirm').click()
        time.sleep(1)
        driver.find_element_by_css_selector('#rspns011').click()
        driver.find_element_by_css_selector('#rspns02').click()
        driver.find_element_by_css_selector('#rspns070').click()
        driver.find_element_by_css_selector('#rspns080').click()
        driver.find_element_by_css_selector('#rspns090').click()
        driver.find_element_by_css_selector('.btn_blue.btn_block.search_btn').click()
        
    else:
        print("건강하다면 위에 체크한것을 해제하시고 나는 건강하다를 한번만 다시 눌러주세용~")




def K():
    c1 = CheckVariety_1.get()
    c2 = CheckVariety_2.get()
    c3 = CheckVariety_3.get()
    c4 = CheckVariety_4.get()
    c5 = CheckVariety_5.get()

    if c1 ==1 or c2==1 or c3 ==1or c4 ==1 or c5 == 1 :
          print("학교 가기 싫니???")

          
 

checkbutton1=tkinter.Checkbutton(window, text="학생의 몸에 열이 있나요? ", variable=CheckVariety_1,command= lambda: K())
checkbutton2=tkinter.Checkbutton(window, text="학생에게 코로나 19가 의심되는 증상이 있나요? ", variable=CheckVariety_2,command= lambda: K())
checkbutton3=tkinter.Checkbutton(window, text="학생이 최근(14일 이내) 해외여행을 다녀온 사실이 있나요? ", variable=CheckVariety_3,command= lambda: K())
checkbutton4=tkinter.Checkbutton(window, text="동거가족 중 최근 해외여행을 다녀온 사실이 있나요? ", variable=CheckVariety_4,command= lambda: K())
checkbutton5=tkinter.Checkbutton(window, text="동거가족 중 현재 자가격리 중인 가족이 있나요? ", variable=CheckVariety_5,command= lambda: K())
checkbutton6=tkinter.Checkbutton(window, text="위에 증상에 해당하지 않고 나는 건강하다!!!", variable=CheckVariety_6,command= lambda: A())


checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
checkbutton4.pack()
checkbutton5.pack()
checkbutton6.pack()


window.mainloop()












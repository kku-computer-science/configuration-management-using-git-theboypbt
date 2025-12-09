[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9R7rdwse)

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21987154)

---

โปรเจกต์นี้เป็นส่วนหนึ่งของวิชา CP353004 Software Engineering  
กิจกรรม Lab 3.3: Working with Collaborators  
ภาคการศึกษา 2/2568

---

## สมาชิกทีม

- ศิวภาส ภูศรีอ่อน (663380026-5) : ทำในส่วน Algorithms ทั้งหมด (Quick Sort และ Bubble Sort)
- ภควรรธ บุญเรือง (663380227-5) : ทำในส่วนของการรับค่า input integer และ การเลือกการแสดงผลของ Algorithm
- รัชภูมิ ทองแดง (663380231-4) : ทำในส่วนของการแสดงผล Output และการทำงานของโค้ดทั้งหมดใน Main.py

**หมายเหตุ: ส่วนของ Contributors: Siwapad และ PunKunGG เป็นคนๆเดียวกัน เนื่องจากในการเชิญเผลอเชิญผิดบัญชีครับ**

---

## โครงสร้างโปรเจกต์
```
MiniProjectLab3/
│── input.py               # ฟังก์ชันการรับข้อมูลตัวเลขและเลือกการ sort ข้อมูล
│── sort_algorithms.py     # ฟังก์ชันการทำงานของ Algorithms ทั้งสอง
│── output.py              # ฟังก์ชั่นการแสดงผล
│── main.py                # โปรแกรมหลัก แสดงผลและเลือกอัลกอริทึม
```

---

![hippo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzN3d3NxcXF0YXAzeGw0aHMzcDF5eHJmcWxpemhmbWhyanl6eDR3NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2IudUHdI075HL02Pkk/giphy.gif)

## ขั้นตอนการรันทดสอบโปรแกรม

**1. ให้ทำการ clone repository ลงไปในเครื่อง โดยคำสั่ง**

``` git clone https://github.com/kku-computer-science/configuration-management-using-git-theboypbt.git ```

---

**2. เปิดโฟลเดอร์โดยใช้โปรแกรม Visual Studio Code**

<img width="295" height="367" alt="image" src="https://github.com/user-attachments/assets/fafc2d28-1777-456a-b217-9155e1f6e996" />

---

**3. เลือกไฟล์ main.py และทำการกดรัน จะเห็นข้อความใน Terminal ให้ผู้ใช้ใส่ค่าตัวเลขโดยการใส่หลายค่าจะต้องทำการเว้นช่องว่าง**

<img width="619" height="167" alt="image" src="https://github.com/user-attachments/assets/2b96dd2d-45b5-4b27-941d-a052d4bfa27d" />

---

**4. หลังจากใส่ค่าทั้งหมดแล้วผู้ใช้ต้องเลือกการ Sorting ข้อมูลโดยสามารถใช้เป็น (1, b, bubble) เพื่อแทนการเลือกการจัดเรียงแบบ Bubble และ (2, q, quick) เพื่อแทนการเลือกการจัดเรียงแบบ Quick หลังจากนั้นโปรแกรมจะทำการ sort ข้อมูลและแสดงผลลัพธ์ให้ผู้ใช้**

<img width="531" height="68" alt="image" src="https://github.com/user-attachments/assets/95d45864-6e7c-4947-b6a0-116e0c7cb737" />

<img width="574" height="98" alt="image" src="https://github.com/user-attachments/assets/2468c355-6725-4d26-a9f1-c469e9089cee" />

---

**กรณีที่ผู้ใช้กรอก หรือ ใส่ข้อมูลผิดจะทำให้โปรแกรมทำงานต่อ แต่ไม่ได้เรียงค่าตัวเลขให้**

<img width="564" height="83" alt="image" src="https://github.com/user-attachments/assets/fbc5083a-f8e7-4a09-81a4-4086463100f3" />

---

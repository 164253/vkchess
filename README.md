# vkchess
這裡是科摩多龍棋的程式碼  
我們的網站是vkchess.pythonanywhere.com(暫時使用)  
我 也就是主要的程式碼維護人 是科摩多龍製作團隊中的犰狳  
底下的程式碼皆會有我個人製作的影片介紹與分析  
將放在youtube https://www.youtube.com/channel/UCqJ-zg12p429fH_9G-5aTQQ  
和bilibili https://space.bilibili.com/284811475  

本專案採用的許可證由我個人撰寫於license檔案中 使用此專案任何程式碼者皆視為同意此許可證  
對本github.com/164253/vkchess下所有程式碼有效  

底下為現有程式碼介紹  
各目錄下都會有講述建構與依賴的setting文檔  
還有一個版本更新的version檔  
/cvkc 娛樂+最小化性質測試的  
使用c語言編寫 一檔即完成全部功能 輸出採用stdout  
/cvkdll 單機和網頁的內核 最常用  
使用c語言編寫 一樣是一檔完成 雖然名字叫dll但其實編譯成so不會有語法問題  
因為我使用win10-64bit所以沒編so 有需要可以直接使用setting中的編譯方式自行生成  
/cvkpy 現行最常用的單機版  
使用python 並用ctypes引入cvkdll得到結果後顯示  
/flask 新的網頁版 但是沒伺服器能用  
使用python-flask以及socketio 然後加上cvkdll 是人類現在的希望(  
還在等待google cloud或別的免費支援socketio的伺服器  
/flask_without_socketio 現行最常用的網頁版  
使用python-flask加上cvkdll 由於用了一堆ajax再加長輪巡 是真實的效能毀滅者(  
/jsvk 廢棄版本  
將cvkc轉為js並加上pyvk的畫面顯示的js版 是剛開始網頁環境測試的時候弄的  
好處是瀏覽器就能跑 但相對不能用來實作於網站  
/phpvk 廢棄版本  
因為不知道為甚麼寫出來的(  
是jsvk換成php的版本 避免了更改原代碼的問題 但是真的很慢  
是目前唯一還有bug不能跑的版本  
/pyvk 舊單機版 因為能上一步所以還是廣泛使用  
純python 最一開始的版本 構建了後來所有版本的基礎  
因為效能問題才轉為cvkpy版 曾試著用cython但發現gui會很麻煩 所以暫時放著了  
未來某天會再重新優化的  
/javavk(名稱未定) 製作中  
新路線 為了android而開始的 雖然也有其他實現方式 不過就是會想試一下用kotlin寫嘛(  

後記  
關於檔案的發展史  
一開始為了方便寫了pyvk 後來效能看不下去 就寫了cvkc 然後為了躲過qt跟opengl 用了cvkdll+cvkpy的組合實現  
接著到了科摩多龍棋在現實上擴張 有線上下棋的需求 寫了個jsvk做測試 不過當然這種客戶端運算做不了伺服器  
所以改出phpvk(並且發現一點用都沒有) 再後來就產生了python-flask的系列 結果卻因為pythonanywhere不支援socketio  
造成我還在尋找免費伺服器的路 現在試著弄google cloud 不過讀文檔的痛苦就那樣  
所以有生之年應該可以讓flask下不是without-socketio的那份檔案活起來  

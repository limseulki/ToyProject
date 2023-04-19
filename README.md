# ToyProject
우리들의 레시피
> 우리들의 레시피는 본인만의 노하우가 담긴 요리 레시피를 공유하는 게시판 형태의 웹 페이지 입니다.

# 유튜브 시연 영상
![우리들의레시피_썸네일](https://user-images.githubusercontent.com/97998858/232944484-80f0027a-e4d4-464e-a07d-8af8e28d298d.png)

https://youtu.be/Y-vXxqDjDpU

# 와이어 프레임
> 메인페이지
1. 메인 페이지에는 로그인 / 회원가입 / 레시피 등록 버튼이있으며 각 버튼을 누르면 해당 페이지로 이동
2. 레시피는 카드 형태의 게시물로 업로드되고 사진을 누르면 해당 레시피 상세 페이지로 이동
![image](https://user-images.githubusercontent.com/97998858/232943575-bf3e8ab3-937d-4410-8e03-c9e787559e12.png)

> 회원가입 페이지
1. 회원가입 페이지에서는 아이디 / 비밀번호 / 이름 or 닉네임 정보를 받아서 회원 가입을 진행
2. 회원 가입이 완료되면 가입완료 팝업뜨고 메인 페이지로 이동
3. 메인페이지 버튼을 누르면 메인 페이지로 이동 (작성중 내용 저장X)
![image](https://user-images.githubusercontent.com/97998858/232943652-f735f43f-d7c6-43e9-b4cd-37e1d779e741.png)

> 로그인 페이지
1. 아이디 / 비밀번호를 입력해서 로그인
2. 메인페이지 버튼을 누르면 메인 페이지로 이동
![image](https://user-images.githubusercontent.com/97998858/232943722-db5a5749-d182-4611-a492-84d6c99ec3ed.png)

> 레시피 상세페이지
1. 해당 레시피의 사진과 레시피 내용이 보임
2. 작성자가 삭제 버튼을 누르면 경고창이 뜨고(’정말 삭제하시겠습니까?) 삭제 가능
3. 목록 버튼을 누르면 메인 페이지로 이동(수정된 내용 저장X)
4. 내용 수정하고 수정 버튼을 누르면 반영 완료
5. 댓글 버튼을 누르면 숨겨져있던 댓글 목록과 댓글 입력창이 나옴 (댓글 입력/수정/삭제)
![image](https://user-images.githubusercontent.com/97998858/232943803-2d388008-8f98-4d64-a072-465880c7317d.png)

> 댓글창
1. 레시피 상세 페이지에서 댓글 입력창 버튼을 누르면 숨어 있던 댓글들이 보임
2. 댓글들은 리스트 형식으로 쌓임
3. 각 댓글들은 닉네임이 표기되고 작성자에 한해 수정 또는 삭제가 가능함
4. 댓글 입력창은 최하단에 있고 텍스트 입력 후 등록 가능
5. 등록 버튼을 누르면 등록 완료 팝업과 함께 댓글이 등록 됨
![image](https://user-images.githubusercontent.com/97998858/232943828-4285bf75-d401-487b-b3af-bad66519be3b.png)

> 레시피 등록
1. 요리 사진을 url을 입력하여 등록
2. 요리명과 상세레시피 입력
3. 목록 버튼을 누르면 메인 페이지로 이동 (작성중 내용 저장X)
4. 레시피 url, 요리명, 레시피 내용을 입력 후 등록 버튼을 누르면 ‘등록완료’ 팝업과 함께 메인 페이지로 자동 이동
![image](https://user-images.githubusercontent.com/97998858/232943897-2261a520-4ac0-42ee-84a2-dfe4daa12022.png)

> 레시피 수정
1. 게시물의 수정은 해당 게시물 작성자만 가능
2. url / 요리명 / 레시피 내용 수정 가능
3. 목록 버튼을 누르면 메인 페이지로 이동 (작성중 내용 저장X) 경고창 띄워주면 좋을 듯
4. 내용 입력 후 수정 버튼을 누르면 ‘수정 완료’ 팝업과 함께 메인 페이지로 이동
![image](https://user-images.githubusercontent.com/97998858/232943965-f1766a62-0fbc-4730-8803-2b616cc37cb7.png)

# API 명세서
![image](https://user-images.githubusercontent.com/97998858/232944077-288ea77b-efe2-44d2-93da-5d72102d89b5.png)


노션 링크
https://www.notion.so/27-65a65e1d2a7e4e8f83a386697199bb35
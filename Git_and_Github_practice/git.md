# 깃이란 뭘까?

1. 분산 버전 관리 시스템
    1. 버전 관리?
        * 코드의 히스토리(버전)을 관리하는 도구
        - 개발되어온 과정을 파악 가능


    1. 분산?
        - 분산의 반댓말 ==  중앙 집중
            - 한곳에 모인곳
            **만약 이곳에 데이터가 날아간다면?**
            분산 시켜야한다.
            *모두가 나눠서 보관한다*
            **복사본을 여럿이 들고 있으니, 조작이 안된다**


>깃은 버전 관리를 추가시켜뒀다
>>근데 변경 사항만 기억을 한다
>>>왜? 효율적이라서.

파일은 그대로 두고, 변경사항만 각 버전으로 가지고 잇다.


![git](img\git1.png)


**버전의 데이터 만 가지고 있다면, 
최종본도 결과적으로 분산적으로 가질 수 있다.**



-----
깃이란 
이러한 저장공간을 제공한다

ex) github/ gitlab/ bigbucket 등등


-----

1. 깃은
    1. 분산 버전 관리 시스템이고


2. 깃허브는
    1. 깃 기반의 저장소 서비스이다.


깃 배시 명령어

1. `ls` 현재 위치의 폴더, 파일 목록 보기
2. `ls -al` 현재 위치의 숨심 파일을 포함하여 보기
3. `pwd` 현재 위치 보기
3. `cd {path}` 현재 위치 이동하기
    1. `cd . .` 상위 폴더로 이동하기
4. `mkdir {name}` 폴더 생성하기
5. `touch {name}` 파일 생성하기
6. `rm {name}` 삭제하기
    1. `rm - r {name}` 폴더 삭제하기


clear 사용시 다 지워짐
enter 누르면 맨 밑으로

``` ``바탕 화면`` ```

``` start . ``` 디렉토리 열기


깃의 세 가지 영역

- working directory - staging area - repository

1. workiung directoty : 현재 나의 폴더 (깃 연결한 폴더)
2. staging area : 앞으로 내가 commit으로 남기고 싶은 파일이 있는 곳? 
3. repository :  commit 들이 저장되는 곳



새로 만들기 >  git add > git commit

working directory에서 파일생성
staging area에서 git add로 tracked 상태 만들기
git commit으로 committed 하기


이때, 수정을 한다면 modified 상태가 된다.

git add 를 통해서 다시 올리고

git commit으로 다시 쌓기


git add 는 버전 생성하기


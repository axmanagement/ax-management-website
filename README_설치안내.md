# AX경영연구소 CMS 설치 안내

## 준비된 기능
- 홈페이지 기존 구성 유지 + 반응형 칼럼·인사이트 게시판
- 제목/본문 검색, 분야 필터, 개별 글 보기, 사진 표시
- `/admin/`에 Sveltia CMS 관리자 화면: 글 작성·수정·삭제, 이미지 첨부, 공개 여부
- CMS가 GitHub에 Markdown 파일을 저장하면 Netlify가 자동 재배포

## 중요: ZIP 수동 업로드만으로는 관리자 저장 기능이 작동하지 않습니다
CMS는 GitHub 저장소와 Netlify의 Git 연동 및 OAuth 설정이 필요합니다.

### 최초 연결 순서 (PC 권장)
1. GitHub에 계정을 만들고 **비공개 또는 공개** 저장소 `axmanagement-site`를 생성합니다.
2. 이 ZIP을 압축 해제한 뒤 **내용물 전체**를 GitHub 저장소의 `main` 브랜치에 올립니다.
3. `admin/config.yml`의 `YOUR_GITHUB_USERNAME/axmanagement-site`를 실제 `사용자명/저장소명`으로 수정하고 커밋합니다.
4. Netlify에서 현재 사이트 `axmanagement`를 열고 **Git 저장소 연결**을 설정합니다. 기존 사이트와 연결이 어렵다면 새 사이트로 배포한 후 기존 주소를 이전해야 할 수 있습니다. 빌드 명령은 `python3 scripts/build.py`, 게시 폴더는 `.`입니다.
5. GitHub → Settings → Developer settings → OAuth Apps → New OAuth App에서 생성: 홈페이지 주소 `https://axmanagement.netlify.app`, Authorization callback URL `https://api.netlify.com/auth/done`.
6. GitHub에서 Client ID/Client Secret 발급 후 Netlify의 해당 사이트 → Project configuration → Security → OAuth → GitHub 제공자에 입력합니다. **비밀키를 대화창이나 공개 저장소에 올리지 마세요.**
7. 배포가 끝나면 `https://axmanagement.netlify.app/admin/`에서 GitHub 로그인 후 글을 작성합니다. GitHub 저장소 쓰기 권한이 있는 계정만 편집 가능합니다.
8. 글 저장 → GitHub 커밋 → Netlify 자동 재배포 → 공개 게시판 반영 순서로 작동합니다.

### 게시물·사진
- 칼럼: `posts/*.md`에 저장
- 첨부 사진: `images/`에 저장
- 공개 글 목록: Netlify 빌드가 생성하는 `posts.json`
- 공개 여부를 끄면 빌드된 목록에 포함되지 않습니다. **단, 공개 GitHub 저장소에서는 원본 초안 파일이 보일 수 있습니다.** 비공개 저장소를 권장합니다.

### 현재 상태
홈페이지 및 관리자 화면 코드는 제작됐지만 GitHub 연결·OAuth 인증은 아직 진행되지 않았습니다. 이 단계가 끝나기 전에는 로그인/글 저장이 불가능합니다.

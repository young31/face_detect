# 사진들을 직접 모으는 작업부터 테스트하는 작업까지 모든 절차를 담은 패키지입니다.
해당 패키지의 모든 작업을 진행하시려면 dlib, opecCV, keras가 필요합니다.
dlib이 현재 3.6버전까지만 지원한다고 하니 버전에 유의하시기 바랍니다. 
각 인원별 사진의 양이 다수가 아니라고 가정하고 진행하였습니다.  
[웹서비스코드](https://github.com/jngmk/keras_image)
## 1. crawling 

crawling에는 두 가지 함수가 포함되어 있습니다.

- crawling: 구글에 검색한 이미지를 원하는 수 만큼 저장합니다.
            이 과정에서 꼭 저장하려고 한만큼 저장되지 않는 경우가 많이 발생하는데 이는 구글의 자체적 제약으로 보입니다.
            다수의 이름은 리스트로 받습니다.
            
- sorting: 크롤링한 사진들은 우리가 원하는 자료만 있지 않습니다. 그 중 이 후 처리하는데 편의를위해 자료형을 jpg만 남기고 삭제합니다.
           자료형은 원하는대로 정하실 수 있습니다.
           이는 처리해야 할 많은 작업중 일부에 대해 편의를 제공합니다.

## 2. face detect & crop

crop(predictor, name, from_dir, to_dir, rename=True) 의 형식으로 사용합니다.  
predictor는 dlib에서 다운로드 받으실 수 있습니다. [링크](https://github.com/davisking/dlib-models) 
또는 업로드된 파일을 받으셔서 사용하셔도 됩니다.

위 명령어는 대상 디렉토리의 이름을 모두 <name>.<index>.jpg 형태로 만드는 작업을 자동으로 함께 지원해 줍니다.  
rename = False로 함으로 이 작업을 중복으로 실행하는 것을 막을 수 있습니다.  

사진 자료의 알수없는 포맷 에러가 발생하는 경우 패스하도록 try, except 구문을 사용하였습니다.  

## 3. modeling

preprocessing과 pre_trained 모형을 간편하게 사용할 수 있도록 세팅하였습니다.  
이 절차는 모두 편의를 위한 것이며 직접 customize하시는 것을 권장드립니다.  

### 3-1. prerpocessing
keras가 제공하는 generator함수를 사용합니다.  
train과 val(test)가 나뉘어져 있으며 train의 경우 다양한 변화를 만들어 내도록 설계하였습니다.  

### 3-2. pre-trained model
keras에서 사용할 수 있는 모형을 담았습니다.  
face 관련 모형은   
<<pip install git+https://github.com/rcmalli/keras-vggface.git >>
를 사용하여 다운받으신 후 사용가능합니다.  
VGG16_face모형과 Inception_V3 모형은 확인하였고 resnet등의 모형은 작업환경의 한계로 테스트해보지 못하였습니다.  

모형을 사용하시고 절차대로 compile과 fit을 통해 훈련시키시면 됩니다.  

## 4. testing
모형이 충분히 훈련된 상태에서 실제 서비스에 사용할 코드 입니다.  
사용자에게서 사진을 한 장 받은 후 이를 내부적으로 얼굴부분만 따로 분리하여 모형을 통해 가장 가까운 인물의 결과를 보여줍니다.  
모형에 사용한 class들 중 어떤 인물과 가장 가까운지 알 수 있습니다. 

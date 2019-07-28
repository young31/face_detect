import numpy as np
import keras

def prerpocessing(train_dir, val_dir, test_dir, size=224):
    from keras.preprocessing.image import ImageDataGenerator

    train_data_gen = ImageDataGenerator(zoom_range= 0.1,
                                        width_shift_range= 10,
                                        height_shift_range= 10,
                                        rescale = 1/255
                                       )
    data_gen = ImageDataGenerator(rescale=1/255)

    train_gen = train_data_gen.flow_from_directory(train_dir,
                                            target_size=(size,size),
                                            batch_size=100,
                                            class_mode='categorical')
    val_gen = data_gen.flow_from_directory(val_dir,
                                            target_size=(size,size),
                                            batch_size=50,
                                            class_mode='categorical')
    
    test_gen = data_gen.flow_from_directory(test_dir,
                                        target_size=(size,size),
                                        batch_size=50,
                                        class_mode='categorical')
    
def VGG16_face(classes, size, hidden=512):
    from keras_vggface.vggface import VGGFace
    from keras.engine import  Model
    from keras.layers import Flatten, Dense, Input
    from keras_vggface.vggface import VGGFace
    
    vgg_model = VGGFace(model='vgg16', include_top=False, input_shape=(size, size, 3))
    last_layer = vgg_model.get_layer('pool5').output
    x = Flatten(name='flatten')(last_layer)
    x = Dense(hidden, activation='relu', name='fc6')(x)
    x = Dense(hidden, activation='relu', name='fc7')(x)
    out = Dense(classes, activation='softmax', name='fc8')(x)
    model = Model(vgg_model.input, out)
    
    return model

def VGGRES_face(classes, size=224):
    from keras_vggface.vggface import VGGFace
    from keras.engine import  Model
    from keras.layers import Flatten, Dense, Input
    from keras_vggface.vggface import VGGFace

    vgg_model = VGGFace(model='resnet50', include_top=False, input_shape=(size, size, 3))
    last_layer = vgg_model.get_layer('avg_pool').output
    x = Flatten(name='flatten')(last_layer)
    out = Dense(classes, activation='softmax', name='classifier')(x)
    model = Model(vgg_model.input, out)
    
    return model

def VGGNES_face(classes, size=224):
    from keras_vggface.vggface import VGGFace
    from keras.engine import  Model
    from keras.layers import Flatten, Dense, Input
    from keras_vggface.vggface import VGGFace
    
    vgg_model = VGGFace(model='nesnet50', include_top=False, input_shape=(size, size, 3))
    last_layer = vgg_model.get_layer('avg_pool').output
    x = Flatten(name='flatten')(last_layer)
    out = Dense(classes, activation='softmax', name='classifier')(x)
    model = Model(vgg_model.input, out)
    
    return model

def V3(classes, size=224):
    from keras_vggface.vggface import VGGFace
    from keras.engine import  Model
    from keras.layers import Flatten, Dense, Input
    from keras_vggface.vggface import VGGFace
    from keras.applications import inception_v3

    model = inception_v3.InceptionV3(include_top=False, input_shape=(size,size,3), classes=classes)

    last_layer = model.get_layer('mixed10').output
    x = Flatten(name='flatten')(last_layer)
    out = Dense(classes, activation='softmax', name='classifier')(x)
    model = Model(model.input, out)
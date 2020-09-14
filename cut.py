from PIL import Image
import cv2
import glob
import os
#im = Image.open('Images/003/watanabe001.jpg')

# 真ん中周辺をトリミングする
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))

# センタリングを行う
def centering(path):
    im = Image.open(path)
    im_new = crop_center(im,1600, 1600)
    return im_new

# リサイズを行う
def resize(path):
    img = cv2.imread(path)
    im_new_resize = cv2.resize(img, (640,640))
    return im_new_resize

# ディレクトリ内のすべての画像をセンタリングする
def bundle_centering(dir):
    path_list = glob.glob('Images/005/*')
    name_list = []
    ext_list = []

    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        name_list.append(name)
        ext_list.append(ext)

        output_path = os.path.join(*['Images/tmp', name + ext])
        img = centering(i)
        img.save(output_path, quality=95)
#        cv2.imwrite(output_path,img)
    return

# ディレクトリ内のすべての画像をリサイズする
def bundle_resize(dir):
    path_list = glob.glob(dir + '/*')
    name_list = []
    ext_list = []

    for i in path_list:
        file = os.path.basename(i)
        name, ext = os.path.splitext(file)
        name_list.append(name)
        ext_list.append(ext)

        output_path = os.path.join(*['Images/005', name + '_resize' + ext])

        img = resize(i)
        cv2.imwrite(output_path,img)
    return

# remove file in tmp dir
def remove_glob(pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p):
            os.remove(p)

bundle_centering('Images/005')
remove_glob('Images/005/*')
bundle_resize('Images/tmp')
remove_glob('Images/tmp/*')
#im_new.save('Images/003/a.jpg', quality=95)
#img = Image.open('Images/003/a.jpg')
#im_new.save('Images/003/b.jpg', quality=95)
#cv2.imwrite('Images/003/b.jpg', im_new_resize)

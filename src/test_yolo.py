from ultralytics import YOLO
from PIL import Image


project_dir = '/root/yolo'

input_img = '/root/images/traffic.jpg'


def main():
    model = YOLO(project_dir + '/weights/yolov8x.pt')
    results = model.predict(input_img)

    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        im_array = result.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[:, :, ::-1])  # RGB PIL image
        im.save('results.jpg')  # save image


if __name__ == '__main__':
    main()

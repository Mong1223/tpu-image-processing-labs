from HaarTansformation import HaarTransformation


if __name__ == "__main__":
    imageName = "482.jpg"
    # transform = HaarTransformation(imageName)
    # transform.printImageFromBuf('Оригинал')
    # transform.directHaar()
    # transform.printImageFromBuf('Хаар прямое 1')
    # transform.directHaar()
    # transform.printImageFromBuf('Хаар прямое 2')
    # transform.reverseHaar()
    # transform.printImageFromBuf('Хаар обратное 1')
    # transform.reverseHaar()
    # transform.printImageFromBuf('Хаар обратное 2')

    transform = HaarTransformation(imageName)
    transform.printImageFromBuf('Оригинал')
    transform.directDobeshi()
    transform.printImageFromBuf('Добеши прямое 1')
    transform.directDobeshi()
    transform.printImageFromBuf('Добеши прямое 2')
    transform.reverseDobeshi()
    transform.printImageFromBuf('Добеши обратное 1')
    transform.reverseDobeshi()
    transform.printImageFromBuf('Добеши обратное 2')

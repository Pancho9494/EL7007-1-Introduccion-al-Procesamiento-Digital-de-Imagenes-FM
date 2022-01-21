def auto_canny(image, sigma=0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	return edged 



def e_indicator(img_original, img_enhanced):
  no = len(np.where(auto_canny(img_original) == 255)[0])
  nr = len(np.where(auto_canny(img_enhanced) == 255)[0])
  return np.abs(nr-no)/no



def show_img_hist(img_original, img_enhanced, title, Flag_vertical = True):
  # Solamente para mostrar en matplotlib, se transforma a RGB.
  
  #NOTA! Elimine la linea plt.show() de su función plot_histogram_rgb para que 
  #funcione correctamente esta linea. 

  # Lectura de la imagen original:
  b, g, r = cv2.split(img_original)
  img_matplotlib_original = cv2.merge([r,g,b])

  # Lectura de la imagen procesada:
  b, g, r = cv2.split(img_enhanced)
  img_matplotlib_enhanced = cv2.merge([r,g,b])

  if Flag_vertical:
    fig, ax = plt.subplots(2, 3, figsize=(15,7))

    plt.subplot(1, 3 , 1);
    plt.imshow(img_matplotlib_original); plt.axis('off')
    plt.title('Imagen Original')

    plt.subplot(1, 3 , 2);
    plt.imshow(img_matplotlib_enhanced); plt.axis('off')
    plt.title('Imagen Procesada por: ' + title)

    plt.subplot(2, 3, 3);
    plot_histogram_rgb(img_original);
    plt.title('Histograma de la Imagen Original')

    plt.subplot(2, 3, 6);
    plot_histogram_rgb(img_enhanced);
    plt.title('Histograma de la Imagen por: ' + title)
  else:
    fig, ax = plt.subplots(2, 2, figsize=(15,7))

    plt.subplot(2, 2 , 1);
    plt.imshow(img_matplotlib_original); plt.axis('off')
    plt.title('Imagen Original')

    plt.subplot(2, 2 , 2);
    plt.imshow(img_matplotlib_enhanced); plt.axis('off')
    plt.title('Imagen Procesada por: ' + title)

    plt.subplot(2, 2, 3);
    plot_histogram_rgb(img_original);
    plt.title('Histograma de la Imagen Original')

    plt.subplot(2, 2, 4);
    plot_histogram_rgb(img_enhanced);
    plt.title('Histograma de la Imagen por: ' + title)

  plt.show()
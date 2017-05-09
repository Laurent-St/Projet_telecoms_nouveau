def show_thermal_image(self, filename):
    global db_ext, gallery_folder
    f = open(filename)
    lines = f.readlines()
    f.close()
    ypixel = len(lines)
    if ypixel != 0:
        xpixel = len(lines[0].split(","))
        if xpixel != 0:
            data = np.zeros((xpixel, ypixel))
            for i in range(ypixel):
                line = lines[i].strip().split(",")
                for j in range(xpixel):
                    data[i,j] = float(line[j])
            plt.clf()
            cmap = get_cmap('jet')
            plt.imshow(data, interpolation="nearest", cmap=cmap)
            plt.axis('off')
            cb = plt.colorbar()
            cb.set_label('Temp (in C)  ')
            database_file = gallery_folder + "/" + path.basename(filename)
            if not path.exists(database_file):
                plt.savefig(database_file.replace(db_ext ,".png"))
            plt.show()

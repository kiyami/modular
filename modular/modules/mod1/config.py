
contents = {

    "sahıs_tipi": {
        0: ["Danışman", "Danışan"],
    },

    "isim": {
        0: ["Kıyami", "Sungur", "Saliha"],
        1: ["Ali", "Veli", "Ayşe"]
    },

    "h_ici": {
        0: ["Pzts", "Salı", "Çarş", "Perş", "Cuma"],
    },

    "h_sonu": {
        0: ["Cts", "Pzr"],
    },

}


relations = {
    0: ["sahıs_tipi", (0,0), "isim", 0],
    1: ["sahıs_tipi", (0,1), "isim", 1],
}


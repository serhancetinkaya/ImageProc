private void RGBSlicing_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, CikisResmi;
    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    CikisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);

    int Eşik1 = 100; // Kırmızı (R) için eşik değeri
    int Eşik2 = 150; // Yeşil (G) için eşik değeri
    int Eşik3 = 200; // Mavi (B) için eşik değeri

    for (int x = 0; x < ResimGenisligi; x++)
    {
        for (int y = 0; y < ResimYuksekligi; y++)
        {
            OkunanRenk = GirisResmi.GetPixel(x, y);

            int R = OkunanRenk.R;
            int G = OkunanRenk.G;
            int B = OkunanRenk.B;

            // Kırmızı (R) kanal için bölütlenme
            if (R >= Eşik1)
            {
                R = 255;
            }
            else
            {
                R = 0;
            }

            // Yeşil (G) kanal için bölütlenme
            if (G >= Eşik2)
            {
                G = 255;
            }
            else
            {
                G = 0;
            }

            // Mavi (B) kanal için bölütlenme
            if (B >= Eşik3)
            {
                B = 255;
            }
            else
            {
                B = 0;
            }

            CikisResmi.SetPixel(x, y, Color.FromArgb(R, G, B));
        }
    }

    pictureBox2.Image = CikisResmi;
}

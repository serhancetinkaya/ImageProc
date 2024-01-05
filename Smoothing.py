private void Smoothing_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, YumusatilmisResmi;
    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    YumusatilmisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);

    int SablonBoyutu = 3;

    int[,] SmoothingMatris = { { 1, 1, 1 }, 
                               { 1, 1, 1 }, 
                               { 1, 1, 1 } };

    int x, y, i, j, Gri, Toplam;

    for (x = (SablonBoyutu - 1) / 2; x < ResimGenisligi - (SablonBoyutu - 1) / 2; x++)
    {
        for (y = (SablonBoyutu - 1) / 2; y < ResimYuksekligi - (SablonBoyutu - 1) / 2; y++)
        {
            Toplam = 0;

            // Şablon bölgesi (çekirdek matris) içindeki pikselleri tarar.
            int k = 0; // Matris içindeki elemanları sırayla okurken kullanılır.
            
            for (i = -((SablonBoyutu - 1) / 2); i <= (SablonBoyutu - 1) / 2; i++)
            {
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyutu - 1) / 2; j++)
                {
                    OkunanRenk = GirisResmi.GetPixel(x + i, y + j);
                    Gri = (OkunanRenk.R + OkunanRenk.G + OkunanRenk.B) / 3;
                    Toplam = Toplam + Gri * SmoothingMatris[k, k];
                    k++;
                }
            }

            Toplam = Toplam > 255 ? 255 : (Toplam < 0 ? 0 : Toplam);

            // Smoothing (Yumuşatma) işlemi uygula
            YumusatilmisResmi.SetPixel(x, y, Color.FromArgb(Toplam, Toplam, Toplam));
        }
    }

    pictureBox2.Image = YumusatilmisResmi;
}

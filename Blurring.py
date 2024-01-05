private void LaplaceBlurring_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, CikisResmi, BlurredResmi;
    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    CikisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);
    BlurredResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);

    int SablonBoyutu = 3;

    int[,] LaplaceMatris = { { -1, -1, -1 }, 
                             { -1,  8, -1 }, 
                             { -1, -1, -1 } };

    int x, y, i, j, Gri, Toplam;

    for (x = (SablonBoyutu - 1) / 2; x < ResimGenisligi - (SablonBoyutu - 1) / 2; x++)
    {
        for (y = (SablonBoyutu - 1) / 2; y < ResimYuksekligi - (SablonBoyutu - 1) / 2; y++)
        {
            Toplam = 0;

            int k = 0; 
            
            for (i = -((SablonBoyutu - 1) / 2); i <= (SablonBoyutu - 1) / 2; i++)
            {
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyutu - 1) / 2; j++)
                {
                    OkunanRenk = GirisResmi.GetPixel(x + i, y + j);
                    Gri = (OkunanRenk.R + OkunanRenk.G + OkunanRenk.B) / 3;
                    Toplam = Toplam + Gri * LaplaceMatris[k, k];
                    k++;
                }
            }

            Toplam = Toplam > 255 ? 255 : (Toplam < 0 ? 0 : Toplam);

            CikisResmi.SetPixel(x, y, Color.FromArgb(Toplam, Toplam, Toplam));
        }
    }

    pictureBox2.Image = CikisResmi;

    // Blurring işlemi
    for (x = 1; x < ResimGenisligi - 1; x++)
    {
        for (y = 1; y < ResimYuksekligi - 1; y++)
        {
            int toplamGri = 0;

            for (i = -1; i <= 1; i++)
            {
                for (j = -1; j <= 1; j++)
                {
                    OkunanRenk = CikisResmi.GetPixel(x + i, y + j);
                    Gri = (OkunanRenk.R + OkunanRenk.G + OkunanRenk.B) / 3;
                    toplamGri += Gri;
                }
            }

            int yeniRenk = toplamGri / 9;
            BlurredResmi.SetPixel(x, y, Color.FromArgb(yeniRenk, yeniRenk, yeniRenk));
        }
    }

    pictureBox3.Image = BlurredResmi;
}

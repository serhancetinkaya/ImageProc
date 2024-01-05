private void SOBEL_KENAR2_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, CikisResmiX, CikisResmiY, CikisResmiXY;

    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    CikisResmiX = new Bitmap(ResimGenisligi, ResimYuksekligi);
    CikisResmiY = new Bitmap(ResimGenisligi, ResimYuksekligi);
    CikisResmiXY = new Bitmap(ResimGenisligi, ResimYuksekligi);

    int SablonBoyutu = 3;
    int ElemanSayisi = SablonBoyutu * SablonBoyutu;
    int x, y, i, j;
    int Gri = 0;

    int[] MatrisX = { -1, 0, 1, -2, 0, 2, -1, 0, 1 };
    int[] MatrisY = { 1, 2, 1, 0, 0, 0, -1, -2, -1 };

    int RenkX, RenkY, RenkXY;

    for (x = (SablonBoyutu - 1) / 2; x < ResimGenisligi - (SablonBoyutu - 1) / 2; x++)
    {
        for (y = (SablonBoyutu - 1) / 2; y < ResimYuksekligi - (SablonBoyutu - 1) / 2; y++)
        {
            int toplamGriX = 0, toplamGriY = 0;

            // Şablon bölgesi (çekirdek matris) içindeki pikselleri tarıyor.
            int k = 0; // matris içindeki elemanları sırayla okurken kullanılacak.

            for (i = -((SablonBoyutu - 1) / 2); i <= (SablonBoyutu - 1) / 2; i++)
            {
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyutu - 1) / 2; j++)
                {
                    OkunanRenk = GirisResmi.GetPixel(x + i, y + j);
                    Gri = (OkunanRenk.R + OkunanRenk.G + OkunanRenk.B) / 3;
                    toplamGriX = toplamGriX + Gri * MatrisX[k];
                    toplamGriY = toplamGriY + Gri * MatrisY[k];
                    k++;
                }
            }

            RenkX = Math.Abs(toplamGriX);
            RenkY = Math.Abs(toplamGriY);
            RenkXY = Math.Abs(toplamGriX) + Math.Abs(toplamGriY);

            RenkX = RenkX > 255 ? 255 : (RenkX < 0 ? 0 : RenkX);
            RenkY = RenkY > 255 ? 255 : (RenkY < 0 ? 0 : RenkY);
            RenkXY = RenkXY > 255 ? 255 : (RenkXY < 0 ? 0 : RenkXY);

            CikisResmiX.SetPixel(x, y, Color.FromArgb(RenkX, RenkX, RenkX));
            CikisResmiY.SetPixel(x, y, Color.FromArgb(RenkY, RenkY, RenkY));
            CikisResmiXY.SetPixel(x, y, Color.FromArgb(RenkXY, RenkXY, RenkXY));
        }
    }

    pictureBox2.Image = CikisResmiX;
    pictureBox3.Image = CikisResmiY;
    pictureBox4.Image = CikisResmiXY;
}

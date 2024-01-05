private void ContraharmonicMean_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, CikisResmi;
    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    CikisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);

    double Q = Convert.ToDouble(textBox1.Text); // Q parametresi, kullanıcıdan alınabilir

    int SablonBoyutu = 3;

    int x, y, i, j, Gri;

    for (x = (SablonBoyutu - 1) / 2; x < ResimGenisligi - (SablonBoyutu - 1) / 2; x++)
    {
        for (y = (SablonBoyutu - 1) / 2; y < ResimYuksekligi - (SablonBoyutu - 1) / 2; y++)
        {
            double ToplamPay = 0;
            double ToplamPayda = 0;

            for (i = -((SablonBoyutu - 1) / 2); i <= (SablonBoyutu - 1) / 2; i++)
            {
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyutu - 1) / 2; j++)
                {
                    OkunanRenk = GirisResmi.GetPixel(x + i, y + j);
                    Gri = (OkunanRenk.R + OkunanRenk.G + OkunanRenk.B) / 3;

                    ToplamPay += Math.Pow(Gri, Q + 1);
                    ToplamPayda += Math.Pow(Gri, Q);
                }
            }

            int yeniRenk = Convert.ToInt32(ToplamPay / ToplamPayda);

            yeniRenk = yeniRenk > 255 ? 255 : (yeniRenk < 0 ? 0 : yeniRenk);

            // Kontraharmonik ortalama işlemi uygula
            CikisResmi.SetPixel(x, y, Color.FromArgb(yeniRenk, yeniRenk, yeniRenk));
        }
    }

    pictureBox2.Image = CikisResmi;
}

private void Sharpening_Click(object sender, EventArgs e)
{
    Color OkunanRenk;
    Bitmap GirisResmi, KeskinleştirilmisResmi;
    GirisResmi = new Bitmap("FltFace.jpg");

    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;

    KeskinleştirilmisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);

    int SablonBoyutu = 3;

    int[,] SharpeningMatris = { { -1, -1, -1 }, 
                                { -1,  9, -1 }, 
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
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyut

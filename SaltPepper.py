private void AddSaltAndPepperNoise_Click(object sender, EventArgs e)
{
    Bitmap GirisResmi, GurultuluResim;
    GirisResmi = new Bitmap("FltFace.jpg");
    GurultuluResim = new Bitmap(GirisResmi);

    Random rand = new Random();
    int saltPepperRatio = 5; // Salt and pepper oranı, isteğinize göre ayarlayabilirsiniz.

    for (int x = 0; x < GirisResmi.Width; x++)
    {
        for (int y = 0; y < GirisResmi.Height; y++)
        {
            int randomValue = rand.Next(100);

            if (randomValue < saltPepperRatio)
            {
                
                GurultuluResim.SetPixel(x, y, Color.White);
            }
            else if (randomValue > (100 - saltPepperRatio))
            {
                
                GurultuluResim.SetPixel(x, y, Color.Black);
            }
        }
    }

    
    pictureBox2.Image = GurultuluResim;
}

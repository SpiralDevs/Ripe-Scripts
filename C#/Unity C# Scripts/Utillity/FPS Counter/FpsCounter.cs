using UnityEngine;
using TMPro;

public class FpsCounter : MonoBehaviour 
{
    private float pollingTime = 1f;
    private float time;
    private int frameCount;
    public TMP_Text FpsCountertxt;

    void Update()
    {
        Counter();
    }

    public void Counter()
    {
        time += Time.deltaTime;
        frameCount++;
        if(time >= pollingTime)
        {
            int frameRate = Mathf.RoundToInt(frameCount / time);
            FpsCountertxt.text = frameRate.ToString() + " FPS";

            time -= pollingTime;
            frameCount = 0;
        }
    }

}
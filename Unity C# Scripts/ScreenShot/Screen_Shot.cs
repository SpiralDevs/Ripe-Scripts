using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Screen_Shot : MonoBehaviour
{

    public void CaptureScreenshot(string filename, int superSize)
    {
        if(Input.GetKey(KeyCode.F12))
        {
            ScreenCapture.CaptureScreenshot("Image Name");
        }else
        {
            return;
        }
    }
}

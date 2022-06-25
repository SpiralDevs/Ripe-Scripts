using UnityEngine;

public class FullScreenSave : MonoBehaviour 
{

    public Toggle fullScreenToggle; // -- UI Toggle 
    public bool fullScreenBool; // -- fullscreen bool

    // -- void
    public void SetFullscreen(bool fullScreen)
    {
        if (fullScreenToggle.isOn == true)
        {
            Screen.fullScreen = true;
            Screen.fullScreen = fullScreen;
            fullScreenBool = fullScreen;
        }else
        {
            Screen.fullScreen = false;
            Screen.fullScreen = fullScreen;
            fullScreenBool = fullScreen;
        }
        PlayerPrefs.SetInt("FullScreenPref", Convert.ToInt32(fullScreenBool));
        Debug.Log("Screen set to " + fullScreen);
        fullScreenBool = fullScreen;
    }

    void Awake()
    {
        fullScreenToggle.isOn = fullScreenBool;
    }

    void Start()
    {
        SetFullscreen(fullScreenBool);
    }
}

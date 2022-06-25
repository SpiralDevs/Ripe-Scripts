using UnityEngine;
using TMPro;
public class Platform : MonoBehaviour 
{
    public TMP_Text platformText;
    void Start()
    {
        string platfromStr = Application.platform.ToString();
        platformText.text = "Platform: " + platfromStr;
    }
}
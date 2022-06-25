using UnityEngine;
using TMPro;

public class Version : MonoBehaviour 
{
    public TMP_Text versionText;
    void Start()
    {
        versionText.text = "Version: v" + Application.version.ToString();
    }
}
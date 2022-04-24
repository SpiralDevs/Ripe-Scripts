using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class CopyToClipboard : MonoBehaviour
{
    public void CopyToTextClipboard()
    {
        string templateString = "Put the text to copy here";
        GUIUtility.systemCopyBuffer = templateString;
    }
}
